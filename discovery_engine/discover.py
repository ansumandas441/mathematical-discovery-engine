#!/usr/bin/env python3
"""
CLI entry point for the theorem discovery engine.

Usage:
    # Dry run (mock workers, no API cost):
    python -m discovery_engine.discover --dry-run "Prove that for any primitive set A, f(A) <= f(primes)"

    # With Claude workers:
    export ANTHROPIC_API_KEY=sk-...
    python -m discovery_engine.discover "Prove that for any primitive set A, f(A) <= f(primes)"

    # With manual start nodes:
    python -m discovery_engine.discover --dry-run \
        --start s_divisibility_definition,s_antichain_in_boolean_lattice \
        --goal "f(A) = sum 1/(a log a) is maximized when A is the set of primes" \
        "Erdős primitive set conjecture"

    # Full LLM orchestration (LLM picks techniques + checks goal):
    python -m discovery_engine.discover --llm-orchestrate "..."

    # Save search tree to file:
    python -m discovery_engine.discover --dry-run --save-tree tree.json "..."
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path


def _fmt_age(ts: float) -> str:
    import datetime
    try:
        return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")
    except (OverflowError, OSError, ValueError):
        return "?"


def _list_problems(registry) -> None:
    rows = registry.list_all()
    if not rows:
        print("No problems registered yet.")
        return
    print(f"{'ID':<14}{'STATUS':<13}{'ITERS':<7}{'UPDATED':<18}PROBLEM")
    print("-" * 92)
    for e in rows:
        problem = (e.get("problem") or "").replace("\n", " ")
        if len(problem) > 40:
            problem = problem[:37] + "..."
        print(
            f"{e['id']:<14}{e.get('status',''):<13}{e.get('iterations',0):<7}"
            f"{_fmt_age(e.get('updated_at', 0)):<18}{problem}"
        )
    print("\nResume any of these by giving the same problem again, "
          "or inspect with --inspect <ID>.")


def _inspect_problem(registry, pid: str) -> int:
    entry = registry.get(pid)
    if entry is None:
        print(f"No registered problem with id {pid}. Use --list-problems.")
        return 1
    print(f"Problem {pid}  (status={entry.get('status')}, iterations={entry.get('iterations')})")
    print(f"  {entry.get('problem','')[:200]}")
    if entry.get("goal"):
        print(f"  Goal: {entry['goal'][:200]}")
    state_path = registry.state_path(pid)
    if not state_path.exists():
        print("\nNo saved search state yet (problem registered but not run).")
        return 0

    from .search_tree import SearchTree

    ckpt = json.loads(state_path.read_text())
    tree = SearchTree.from_dict(ckpt.get("tree", {}))
    print(f"\nSearch mode: {tree.mode}   Tree: {tree.summary()}")
    print("\n=== Per-level attempt ledger (techniques tried at each level) ===")
    tree.print_attempts()
    print("\n=== Search tree ===")
    tree.print_tree()
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Theorem Discovery Engine — search for proofs through the knowledge graph",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("problem", nargs="?", default="", help="The mathematical problem to solve (natural language)")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Use mock workers (no API calls, no cost)",
    )
    parser.add_argument(
        "--use-cli",
        action="store_true",
        help="Use `claude -p` as worker (uses Claude Code subscription, no API key needed)",
    )
    parser.add_argument(
        "--llm-orchestrate",
        action="store_true",
        help="Use LLM for technique selection and goal checking (more expensive)",
    )
    parser.add_argument(
        "--start",
        type=str,
        default=None,
        help="Comma-separated start node IDs (e.g., s_divisibility_definition,s_antichain_in_boolean_lattice)",
    )
    parser.add_argument(
        "--goal",
        type=str,
        default=None,
        help="Goal description (overrides LLM goal parsing)",
    )
    parser.add_argument(
        "--graph",
        type=str,
        default=None,
        help="Path to knowledge_graph.json (default: auto-detect)",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=7,
        help="Maximum search tree depth (default: 7)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=200,
        help="Maximum search iterations (default: 200)",
    )
    parser.add_argument(
        "--candidates",
        type=int,
        default=4,
        help="Number of techniques to try per step (default: 4)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="claude-sonnet-4-20250514",
        help="Claude model for orchestrator (default: claude-sonnet-4-20250514)",
    )
    parser.add_argument(
        "--worker-model",
        type=str,
        default=None,
        help="Claude model for workers (default: claude-haiku-4-5-20251001, ~20x cheaper)",
    )
    parser.add_argument(
        "--save-tree",
        type=str,
        default=None,
        help="Save the search tree to a JSON file",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress progress output",
    )
    parser.add_argument(
        "--print-tree",
        action="store_true",
        help="Print the search tree at the end",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help="Number of parallel workers (default: 2 for --use-cli, 5 for API)",
    )
    parser.add_argument(
        "--resume",
        type=str,
        default=None,
        help="Resume from a checkpoint file (e.g., checkpoints/checkpoint_latest.json)",
    )
    parser.add_argument(
        "--checkpoint-dir",
        type=str,
        default=None,
        help="Directory for periodic checkpoints (enables auto-save every N iterations)",
    )
    parser.add_argument(
        "--checkpoint-every",
        type=int,
        default=5,
        help="Save checkpoint every N iterations (default: 5)",
    )
    parser.add_argument(
        "--bfs",
        action="store_true",
        help="Breadth-first (level-order) search instead of best-first priority search",
    )
    parser.add_argument(
        "--runs-dir",
        type=str,
        default=None,
        help="Directory for the problem registry + per-problem state (default: <repo>/runs)",
    )
    parser.add_argument(
        "--restart",
        action="store_true",
        help="Ignore any saved state for this problem and start fresh",
    )
    parser.add_argument(
        "--list-problems",
        action="store_true",
        help="List all problems the engine has been given (the registry) and exit",
    )
    parser.add_argument(
        "--inspect",
        type=str,
        default=None,
        help="Print the saved state (tree + per-level attempt ledger) for a problem id and exit",
    )

    args = parser.parse_args()

    # Resolve the runs directory (registry + per-problem state live here).
    runs_dir = Path(args.runs_dir) if args.runs_dir else (Path(__file__).resolve().parent.parent / "runs")

    from .registry import ProblemRegistry

    # --- registry-only commands (no graph load needed) ---
    if args.list_problems:
        _list_problems(ProblemRegistry(runs_dir))
        return 0
    if args.inspect:
        return _inspect_problem(ProblemRegistry(runs_dir), args.inspect)

    if not args.problem and not args.resume and not args.goal:
        parser.error("a problem statement or --goal is required (or use --resume to continue from a checkpoint)")
    if not args.problem:
        args.problem = args.goal or ""

    # Import here to avoid slow import on --help
    from .graph import KnowledgeGraph
    from .orchestrator import Orchestrator
    from .worker import CLIWorker, MockWorker, Worker

    # Load graph
    graph_path = args.graph
    if graph_path is None:
        candidate = Path(__file__).resolve().parent.parent / "knowledge_graph.json"
        if candidate.exists():
            graph_path = str(candidate)
        else:
            print("Error: Cannot find knowledge_graph.json. Use --graph to specify path.", file=sys.stderr)
            sys.exit(1)

    print(f"Loading knowledge graph from {graph_path}...")
    t0 = time.time()
    graph = KnowledgeGraph(graph_path)
    print(f"Loaded in {time.time() - t0:.1f}s — {graph.stats()}")

    # Create worker
    if args.dry_run:
        worker = MockWorker()
        print("Mode: DRY RUN (mock workers, no API calls)\n")
    elif args.use_cli:
        cli_parallel = args.workers or 2
        worker = CLIWorker(model=args.worker_model, max_parallel=cli_parallel)
        print("Mode: CLI (uses Claude Code subscription)")
        print(f"  Workers: {cli_parallel} parallel")
        print("  No API key needed — uses your subscription")
        if args.worker_model:
            print(f"  Worker model: {args.worker_model}")
        print()
    else:
        worker_model = args.worker_model or Worker.DEFAULT_MODEL
        worker = Worker(model=worker_model)
        print(f"Mode: LIVE (API)")
        print(f"  Orchestrator model: {args.model}")
        print(f"  Worker model:       {worker_model}")
        if worker_model != args.model:
            print(f"  (workers use cheaper model for ~20x token savings)")
        print(f"  Prompt caching:     ON (system prompts cached for 5 min)\n")

    # --- Registry: recognize seen problems and resume their per-problem state ---
    registry = ProblemRegistry(runs_dir)
    pid = None
    entry = None
    resume_from = args.resume
    checkpoint_dir = args.checkpoint_dir
    state_filename = "checkpoint_latest.json"
    search_mode = "bfs" if args.bfs else "best_first"

    if args.problem:
        pid, entry = registry.register(args.problem, args.goal or "")
        problem_dir = registry.problem_dir(pid)
        state_path = registry.state_path(pid)
        print(f"Problem id: {pid}  (search mode: {search_mode})")
        if not args.checkpoint_dir:
            checkpoint_dir = str(problem_dir)
            state_filename = "state.json"
        if not resume_from:
            if args.restart:
                registry.clear_state(pid)
                print("  --restart: ignoring saved state, starting fresh.")
            elif state_path.exists():
                resume_from = str(state_path)
                print(
                    f"  ✓ Seen before (status={entry['status']}, "
                    f"iterations={entry['iterations']}). Resuming from saved state."
                )
            else:
                print("  New problem — starting fresh.")
        registry.update(pid, status=ProblemRegistry.IN_PROGRESS)

    # Create orchestrator
    api_parallel = args.workers or 5
    orch = Orchestrator(
        graph=graph,
        worker=worker,
        max_depth=args.max_depth,
        max_iterations=args.max_iterations,
        max_parallel_workers=api_parallel,
        candidates_per_step=args.candidates,
        model=args.model,
        verbose=not args.quiet,
        checkpoint_dir=checkpoint_dir,
        checkpoint_every=args.checkpoint_every,
        search_mode=search_mode,
        state_filename=state_filename,
    )

    # Parse start nodes
    start_ids = None
    if args.start:
        start_ids = [s.strip() for s in args.start.split(",")]

    # Resume info
    if resume_from:
        print(f"Resuming from checkpoint: {resume_from}")
    if checkpoint_dir:
        print(f"Checkpointing every {args.checkpoint_every} iterations to {checkpoint_dir}/{state_filename}")

    # Run discovery
    t0 = time.time()
    result = orch.discover(
        problem=args.problem,
        start_node_ids=start_ids,
        goal=args.goal,
        use_llm_for_orchestration=args.llm_orchestrate,
        resume_from=resume_from,
    )
    elapsed = time.time() - t0

    # --- Registry: record outcome ---
    if pid is not None:
        if result.get("found"):
            status = ProblemRegistry.SOLVED
        elif result.get("interrupted"):
            status = ProblemRegistry.INTERRUPTED
        else:
            status = ProblemRegistry.EXHAUSTED
        registry.update(
            pid,
            status=status,
            iterations=result["stats"].get("iterations", 0),
            summary=result["tree"].get("summary", {}),
        )

    # Output
    print(f"\n{'='*60}")
    print(f"Discovery complete in {elapsed:.1f}s")
    print(f"Stats: {json.dumps(result['stats'], indent=2)}")

    if result["found"]:
        print(f"\n★ PROOF PATH FOUND ({len(result['path'])} steps):")
        for i, node in enumerate(result["path"]):
            technique = node.get("technique_applied") or "START"
            desc = node["state"]["description"][:80]
            conf = node["confidence"]
            print(f"  {i}. [{technique}] ({conf:.0%}) {desc}")
    elif result.get("interrupted"):
        print("\n⚠ Search interrupted — state saved.")
        if pid is not None:
            print(f"  Resume by giving the same problem again (id {pid}), "
                  f"or: python -m discovery_engine --inspect {pid}")
        else:
            print(f"  Resume with --resume {resume_from}")
    else:
        print("\n✗ No proof found within search limits.")

    # Token usage report
    tokens = result["stats"].get("tokens", {})
    if tokens and tokens.get("total_input", 0) > 0:
        total_in = tokens["total_input"]
        total_out = tokens["total_output"]
        cache_read = tokens.get("cache_read", 0)
        cache_create = tokens.get("cache_create", 0)
        saved_by_cache = cache_read  # cache reads cost ~10% vs full price
        worker_calls = tokens.get("workers", {}).get("calls", 0)
        print(f"\n--- Token Usage ---")
        print(f"  Input tokens:    {total_in:,}")
        print(f"  Output tokens:   {total_out:,}")
        print(f"  Cache reads:     {cache_read:,} (saved ~90% on these)")
        print(f"  Cache creates:   {cache_create:,}")
        print(f"  Worker calls:    {worker_calls}")
        if total_in > 0:
            cache_pct = (cache_read / (total_in + cache_read + cache_create)) * 100
            print(f"  Cache hit rate:  {cache_pct:.0f}%")

    if args.print_tree:
        print(f"\n{'='*60}")
        print("Search Tree:")
        orch.tree.print_tree()

    if args.save_tree:
        orch.tree.save(args.save_tree)
        print(f"\nSearch tree saved to {args.save_tree}")

    return 0 if result["found"] else 1


if __name__ == "__main__":
    sys.exit(main())
