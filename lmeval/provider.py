"""ModelProvider: the replaceable boundary between lmeval and any language model.

Two implementations: LatxaProvider (live service, needs a key) and ReplayProvider
(recorded answers in tests/fixtures/). Which one runs is chosen by LMEVAL_PROVIDER.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class Answer:
    text: str  # the raw answer, kept as is


@dataclass
class Failure:
    reason: str  # "timeout", "refusal", "unreadable", "no_recorded_answer", ...


class ModelProvider(Protocol):
    def generate(self, prompt: str, params: dict) -> Answer | Failure: ...


class LatxaProvider:
    """Calls the Latxa text API. Reads LATXA_API_URL and LATXA_API_KEY from the environment."""

    def generate(self, prompt: str, params: dict) -> Answer | Failure:
        raise NotImplementedError("US-06, sprint 3")


class ReplayProvider:
    """Returns the recorded answer for a prompt, or Failure('no_recorded_answer')."""

    def generate(self, prompt: str, params: dict) -> Answer | Failure:
        raise NotImplementedError("US-05, sprint 2")
