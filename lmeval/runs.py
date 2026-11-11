"""Run store: saves runs under runs/ as JSON. A saved run is never changed again."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Run:
    id: str
    config: dict  # dataset id and version, prompt, provider, model, params, date
    results: list[dict] = field(default_factory=list)  # one per question: predicted, status, reason, raw


def save(run: Run) -> str:
    raise NotImplementedError("US-03, sprint 2")


def load(run_id: str) -> Run:
    raise NotImplementedError("US-04, sprint 2")


def list_runs() -> list[dict]:
    raise NotImplementedError("US-09, sprint 3")
