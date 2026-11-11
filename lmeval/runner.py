"""Runs an experiment: builds each prompt, asks the provider, maps the answer, records everything."""

from __future__ import annotations

from lmeval.provider import ModelProvider
from lmeval.runs import Run


def run_experiment(experiment: dict, provider: ModelProvider) -> Run:
    raise NotImplementedError("US-05 to US-08, sprint 2")
