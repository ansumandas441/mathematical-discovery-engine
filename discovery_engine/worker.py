"""
Worker module — calls Claude API to attempt a technique on a mathematical state.

Each worker is stateless: it receives (state, technique, goal, context) and
returns a WorkerResult with the new state, confidence, and proof sketch.

Token optimizations:
  - System prompt is static → cached via Anthropic prompt caching (5 min TTL)
  - User prompt trimmed: only 8 context nodes, 3 example inputs/outputs
  - Worker model defaults to Haiku (20x cheaper than Sonnet) — override with
    --worker-model for harder problems
  - Max tokens capped at 1024 for workers (JSON output is compact)
"""

from __future__ import annotations

import json
import os
from typing import Optional

from .search_tree import MathState, WorkerResult

# Static system prompt — marked with cache_control for Anthropic prompt caching.
# This block is sent identically on every worker call, so the API caches it
# after the first call and subsequent calls within 5 minutes get a cache hit
# (paying only 10% of the input token cost for this block).
WORKER_SYSTEM_PROMPT = """\
You are a mathematician. Apply the given technique to the given state. \
Return ONLY JSON:
{"new_state_description":"...","new_state_formal":"...","proof_sketch":"...",\
"confidence":0.0-1.0,"impossible":false,"impossible_reason":"",\
"graph_nodes_used":["..."],"graph_nodes_produced":["..."]}
Confidence: 0.0=guess, 1.0=certain. If technique cannot apply, set \
impossible=true and explain if this is 100% certain or just difficult."""

WORKER_USER_TEMPLATE = """\
State: {state_description}
{state_formal}
Technique: {technique_name} ({cluster_name}, {edge_count} edges)
Inputs: {example_inputs}
Outputs: {example_outputs}
Goal: {goal}
Context: {context}"""

CLUSTER_NAMES = {
    1: "Experimental & Numerical",
    2: "Algebraic Manipulation",
    3: "Symmetry & Invariants",
    4: "Approximation & Limits",
    5: "Abstraction & Axiomatization",
    6: "Topology & Obstruction",
    7: "Self-Reference & Impossibility",
    8: "Iteration & Fixed Points",
    9: "Cross-Field Transfer",
    10: "Computer & Collaboration",
    11: "Probabilistic & Counting",
    12: "Homological & Categorical",
}


def _build_user_prompt(
    state: MathState,
    technique: dict,
    technique_id: str,
    goal: str,
    context_nodes: list[dict],
    graph,
) -> str:
    nbrs = graph.technique_neighbors(technique_id)
    inputs = nbrs.get("inputs", [])
    outputs = nbrs.get("outputs", [])
    edge_count = len(inputs) + len(outputs)
    cluster = graph.get_cluster(technique_id)

    example_in = ", ".join(n.get("name", n["id"]) for n in inputs[:3]) or "none"
    example_out = ", ".join(n.get("name", n["id"]) for n in outputs[:3]) or "none"

    context_str = "; ".join(
        n.get("name", n["id"]) for n in context_nodes[:8]
    ) or "none"

    formal_section = f"\nFormal: {state.formal}" if state.formal else ""

    return WORKER_USER_TEMPLATE.format(
        state_description=state.description,
        state_formal=formal_section,
        technique_name=technique.get("name", technique_id),
        edge_count=edge_count,
        cluster_name=CLUSTER_NAMES.get(cluster, f"Cluster {cluster}"),
        example_inputs=example_in,
        example_outputs=example_out,
        goal=goal,
        context=context_str,
    )


def _parse_response(raw: str, technique_id: str) -> WorkerResult:
    """Parse the LLM JSON response into a WorkerResult."""
    text = raw.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        text = "\n".join(lines)
    try:
        d = json.loads(text)
    except json.JSONDecodeError:
        return WorkerResult(
            new_state=MathState(description=f"[PARSE ERROR] Raw: {text[:200]}"),
            confidence=0.0,
            proof_sketch="",
            impossible=True,
            impossible_reason="Worker returned unparseable response",
            technique_id=technique_id,
        )

    new_state = MathState(
        description=d.get("new_state_description", ""),
        formal=d.get("new_state_formal", ""),
        graph_nodes_used=d.get("graph_nodes_used", []),
        graph_nodes_produced=d.get("graph_nodes_produced", []),
    )
    return WorkerResult(
        new_state=new_state,
        confidence=float(d.get("confidence", 0.0)),
        proof_sketch=d.get("proof_sketch", ""),
        impossible=bool(d.get("impossible", False)),
        impossible_reason=d.get("impossible_reason", ""),
        technique_id=technique_id,
    )


class Worker:
    """
    Calls Claude to apply a single technique to a single state.

    Token optimizations applied:
      1. Default model is Haiku (~20x cheaper than Sonnet, sufficient for
         single-technique application). Use --worker-model to override.
      2. System prompt uses cache_control={"type":"ephemeral"} so the
         Anthropic API caches it across calls. After the first call, all
         subsequent calls within the 5-minute TTL pay only ~10% of the
         input token cost for the system prompt.
      3. Max output tokens capped at 1024 (worker JSON is compact).
      4. User prompt trimmed to ~200-400 tokens (3 examples, 8 context
         nodes, no verbose instructions).
    """

    DEFAULT_MODEL = "claude-haiku-4-5-20251001"

    def __init__(
        self,
        model: str | None = None,
        max_tokens: int = 1024,
        api_key: str | None = None,
    ):
        self.model = model or self.DEFAULT_MODEL
        self.max_tokens = max_tokens
        self._client = None
        self._api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.token_stats = {"input": 0, "output": 0, "cache_read": 0, "cache_create": 0, "calls": 0}

    def _get_client(self):
        if self._client is None:
            import anthropic

            self._client = anthropic.Anthropic(api_key=self._api_key)
        return self._client

    def apply_technique(
        self,
        state: MathState,
        technique_id: str,
        goal: str,
        graph,
    ) -> WorkerResult:
        technique = graph.techniques.get(technique_id, {})

        context_node_ids = state.graph_nodes_used + state.graph_nodes_produced
        context = graph.neighborhood(context_node_ids, radius=2) if context_node_ids else {}
        context_nodes = list(context.values())

        user_prompt = _build_user_prompt(
            state=state,
            technique=technique,
            technique_id=technique_id,
            goal=goal,
            context_nodes=context_nodes,
            graph=graph,
        )

        client = self._get_client()
        response = client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=[
                {
                    "type": "text",
                    "text": WORKER_SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[{"role": "user", "content": user_prompt}],
        )

        self.token_stats["calls"] += 1
        usage = response.usage
        self.token_stats["input"] += getattr(usage, "input_tokens", 0)
        self.token_stats["output"] += getattr(usage, "output_tokens", 0)
        self.token_stats["cache_read"] += getattr(usage, "cache_read_input_tokens", 0)
        self.token_stats["cache_create"] += getattr(usage, "cache_creation_input_tokens", 0)

        raw_text = response.content[0].text
        return _parse_response(raw_text, technique_id)


class CLIWorker:
    """
    Worker that calls `claude -p` via subprocess — uses your Claude Code
    subscription instead of a separate API key.

    No ANTHROPIC_API_KEY needed. Uses the same billing as your Claude Code
    terminal session.

    Caveats vs API Worker:
      - Slightly slower (~2-5s overhead per subprocess spawn)
      - Sequential by default (parallel subprocess calls may hit rate limits)
      - No explicit prompt caching control (Claude Code manages its own cache)
      - Uses your subscription quota
    """

    def __init__(self, model: str | None = None, max_parallel: int = 2):
        self.model = model
        self.max_parallel = max_parallel
        self.token_stats = {"input": 0, "output": 0, "cache_read": 0, "cache_create": 0, "calls": 0}

    def apply_technique(
        self,
        state: MathState,
        technique_id: str,
        goal: str,
        graph,
    ) -> WorkerResult:
        import subprocess

        technique = graph.techniques.get(technique_id, {})
        context_node_ids = state.graph_nodes_used + state.graph_nodes_produced
        context = graph.neighborhood(context_node_ids, radius=2) if context_node_ids else {}
        context_nodes = list(context.values())

        user_prompt = _build_user_prompt(
            state=state,
            technique=technique,
            technique_id=technique_id,
            goal=goal,
            context_nodes=context_nodes,
            graph=graph,
        )

        full_prompt = WORKER_SYSTEM_PROMPT + "\n\n" + user_prompt

        cmd = ["claude", "-p", full_prompt, "--output-format", "json"]
        if self.model:
            cmd.extend(["--model", self.model])

        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120,
            )
            raw_output = proc.stdout.strip()
        except subprocess.TimeoutExpired:
            return WorkerResult(
                new_state=MathState(description="[TIMEOUT]"),
                confidence=0.0,
                proof_sketch="",
                impossible=True,
                impossible_reason="claude -p timed out after 120s",
                technique_id=technique_id,
            )
        except FileNotFoundError:
            return WorkerResult(
                new_state=MathState(description="[ERROR] claude CLI not found"),
                confidence=0.0,
                proof_sketch="",
                impossible=True,
                impossible_reason="claude CLI not found in PATH. Install Claude Code.",
                technique_id=technique_id,
            )

        self.token_stats["calls"] += 1

        result_text = raw_output
        try:
            envelope = json.loads(raw_output)
            result_text = envelope.get("result", raw_output)
            usage = envelope.get("usage", {})
            self.token_stats["input"] += usage.get("input_tokens", 0)
            self.token_stats["output"] += usage.get("output_tokens", 0)
            self.token_stats["cache_read"] += usage.get("cache_read_input_tokens", 0)
            self.token_stats["cache_create"] += usage.get("cache_creation_input_tokens", 0)
        except (json.JSONDecodeError, AttributeError):
            pass

        return _parse_response(result_text, technique_id)


class MockWorker:
    """
    A mock worker for dry-run testing.

    Returns synthetic results based on graph structure — no API calls.
    Useful for testing the orchestrator and search tree without cost.
    """

    def apply_technique(
        self,
        state: MathState,
        technique_id: str,
        goal: str,
        graph,
    ) -> WorkerResult:
        import random

        technique = graph.techniques.get(technique_id, {})
        technique_name = technique.get("name", technique_id)

        nbrs = graph.technique_neighbors(technique_id)
        outputs = nbrs.get("outputs", [])
        inputs = nbrs.get("inputs", [])

        state_ids = set(state.graph_nodes_used + state.graph_nodes_produced)
        relevant_inputs = [n for n in inputs if n["id"] in state_ids]
        relevant_outputs = [
            n for n in outputs
            if n["id"] not in state_ids and n.get("kind") != "technique"
        ]

        if not relevant_outputs:
            relevant_outputs = [
                n for n in outputs if n.get("kind") != "technique"
            ]

        if relevant_outputs:
            pick = random.choice(relevant_outputs[:10])
            desc = f"[{technique_name}] -> {pick.get('name', pick['id'])}"
            new_produced = list(state.graph_nodes_produced) + [pick["id"]]
            confidence = 0.4 + 0.2 * len(relevant_inputs) / max(len(inputs), 1)
        else:
            desc = f"[{technique_name}] (no new outputs reachable)"
            new_produced = list(state.graph_nodes_produced)
            confidence = 0.1

        goal_words = set(goal.lower().split())
        desc_words = set(desc.lower().split())
        if goal_words & desc_words:
            confidence = min(confidence + 0.15, 1.0)

        return WorkerResult(
            new_state=MathState(
                description=desc,
                formal="",
                graph_nodes_used=list(state.graph_nodes_used),
                graph_nodes_produced=new_produced,
            ),
            confidence=round(confidence, 2),
            proof_sketch=f"[MOCK] {technique_name} applied. Produced: {desc}",
            impossible=False,
            technique_id=technique_id,
        )
