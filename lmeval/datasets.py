"""Dataset registry: registered datasets and their versions (data/ is not in Git)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Question:
    id: str
    text: str
    options: dict[str, str]  # {"A": "...", "B": "..."}
    correct: str  # "A"


def get(dataset_id: str, version: str) -> list[Question]:
    raise NotImplementedError("US-01, sprint 2")
