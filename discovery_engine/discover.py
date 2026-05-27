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

    args = parser.parse_args()

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
        checkpoint_dir=args.checkpoint_dir,
        checkpoint_every=args.checkpoint_every,
    )

    # Parse start nodes
    start_ids = None
    if args.start:
        start_ids = [s.strip() for s in args.start.split(",")]

    # Resume info
    if args.resume:
        print(f"Resuming from checkpoint: {args.resume}")
    if args.checkpoint_dir:
        print(f"Checkpointing every {args.checkpoint_every} iterations to {args.checkpoint_dir}/")

    # Run discovery
    t0 = time.time()
    result = orch.discover(
        problem=args.problem,
        start_node_ids=start_ids,
        goal=args.goal,
        use_llm_for_orchestration=args.llm_orchestrate,
        resume_from=args.resume,
    )
    elapsed = time.time() - t0

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
        print("\n⚠ Search interrupted — checkpoint saved. Resume with --resume <path>")
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
