"""
Problem registry — the persistent "list" of problems the engine has been given.

Each problem gets a stable id (hash of its normalized statement + goal) and a
directory under ``runs/<id>/`` holding its resumable state file (``state.json``)
and a human-readable ``problem.md``. The registry itself lives in
``runs/registry.json`` and lets the engine recognize a problem it has seen
before and resume it instead of starting over.
"""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Optional


def normalize(text: str) -> str:
    """Lowercase + collapse whitespace so trivially-different phrasings of the
    same statement hash to the same id."""
    return " ".join((text or "").lower().split())


def problem_id(problem: str, goal: str = "") -> str:
    """Stable 12-hex-char id for a (problem, goal) pair."""
    key = normalize(problem) + "||" + normalize(goal)
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]


class ProblemRegistry:
    """JSON-backed registry of problems and their per-problem run directories."""

    # status values
    NEW = "new"
    IN_PROGRESS = "in_progress"
    INTERRUPTED = "interrupted"
    SOLVED = "solved"
    EXHAUSTED = "exhausted"

    def __init__(self, runs_dir: str | Path):
        self.runs_dir = Path(runs_dir)
        self.runs_dir.mkdir(parents=True, exist_ok=True)
        self.path = self.runs_dir / "registry.json"
        self.data: dict[str, dict] = {}
        if self.path.exists():
            try:
                self.data = json.loads(self.path.read_text())
            except (json.JSONDecodeError, OSError):
                self.data = {}

    # ------------------------------------------------------------------
    # persistence
    # ------------------------------------------------------------------

    def _save(self):
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, indent=2, ensure_ascii=False))
        tmp.replace(self.path)

    # ------------------------------------------------------------------
    # paths
    # ------------------------------------------------------------------

    def problem_dir(self, pid: str) -> Path:
        d = self.runs_dir / pid
        d.mkdir(parents=True, exist_ok=True)
        return d

    def state_path(self, pid: str) -> Path:
        return self.problem_dir(pid) / "state.json"

    # ------------------------------------------------------------------
    # lookup / mutation
    # ------------------------------------------------------------------

    def get(self, pid: str) -> Optional[dict]:
        return self.data.get(pid)

    def find(self, problem: str, goal: str = "") -> Optional[dict]:
        return self.data.get(problem_id(problem, goal))

    def register(self, problem: str, goal: str = "") -> tuple[str, dict]:
        """Return (pid, entry); create the entry the first time we see it."""
        pid = problem_id(problem, goal)
        now = time.time()
        if pid not in self.data:
            self.data[pid] = {
                "id": pid,
                "problem": problem,
                "goal": goal,
                "status": self.NEW,
                "iterations": 0,
                "created_at": now,
                "updated_at": now,
                "state_file": str(self.state_path(pid)),
                "summary": "",
            }
            (self.problem_dir(pid) / "problem.md").write_text(
                f"# Problem {pid}\n\n{problem}\n\n## Goal\n\n{goal or '(same as problem)'}\n",
                encoding="utf-8",
            )
            self._save()
        return pid, self.data[pid]

    def update(self, pid: str, **fields):
        if pid in self.data:
            self.data[pid].update(fields)
            self.data[pid]["updated_at"] = time.time()
            self._save()

    def has_state(self, pid: str) -> bool:
        return self.state_path(pid).exists()

    def clear_state(self, pid: str):
        sp = self.state_path(pid)
        if sp.exists():
            sp.unlink()

    def list_all(self) -> list[dict]:
        return sorted(
            self.data.values(),
            key=lambda e: e.get("updated_at", 0),
            reverse=True,
        )
