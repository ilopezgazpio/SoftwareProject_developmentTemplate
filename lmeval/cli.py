"""Command-line interface: what the researcher types.

Planned commands (see the user stories): register, prompt, experiment, run, list, open, compare, export.
"""

COMPONENTS = {
    "datasets": "dataset registry: get(dataset_id, version)",
    "provider": "ModelProvider interface: generate(prompt, params) -> Answer | Failure",
    "runner": "runs an experiment and records every result",
    "runs": "run store: save(run), load(run_id), list(); never overwrites",
    "compare": "comparator: diff(run_a, run_b) question by question",
}


def main() -> None:
    print("lmeval 0.0.0 · sprint 1 skeleton · nothing implemented yet")
    print("Components (see docs/uml/component-diagram.md):")
    for name, what in COMPONENTS.items():
        print(f"  {name:10} {what}")
