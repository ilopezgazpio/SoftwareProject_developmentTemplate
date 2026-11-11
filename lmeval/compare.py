"""Comparator: pairs two runs by question id and reports where they differ, failures included."""

from __future__ import annotations

from lmeval.runs import Run


def diff(run_a: Run, run_b: Run) -> list[dict]:
    raise NotImplementedError("US-11, sprint 3")
