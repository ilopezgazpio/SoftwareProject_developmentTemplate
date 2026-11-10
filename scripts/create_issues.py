"""Create labels, milestone, issues and the project board on GitHub from the backlog files.

Run once, after the repository exists on GitHub and `gh auth login` is done:

    python scripts/create_issues.py OWNER/REPO            # create everything
    python scripts/create_issues.py OWNER/REPO --dry-run  # only print what would be created

Sources: docs/backlog/product-backlog.md (epics and stories) and docs/sprints/sprint-1-plan.md (tasks).
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LABELS = {
    "epic": "5319e7", "story": "0e8a16", "task": "fbca04",
    "must": "b60205", "should": "d93f0b", "could": "fef2c0",
    "E1": "c5def5", "E2": "c5def5", "E3": "c5def5",
}
MILESTONE = "Sprint 1"
BOARD = "Hiru · Sprint board"


def gh(*args, dry=False):
    cmd = ["gh", *args]
    if dry:
        print("  $", " ".join(a if " " not in a else repr(a) for a in cmd)[:160])
        return ""
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.strip()


def parse_backlog():
    text = (ROOT / "docs/backlog/product-backlog.md").read_text(encoding="utf-8")
    items = []
    for level, head, body in re.findall(r"^(##|###) (.+?)\n(.*?)(?=^## |^### |\Z)", text, re.S | re.M):
        if not re.match(r"(E|US-)\d", head):
            continue
        labels = re.search(r"\*\*Labels:\*\* (.+)", body)
        labels = [l.strip() for l in labels.group(1).split(",")] if labels else []
        items.append((head.strip(), body.strip(), labels, None))
    return items


def parse_tasks():
    text = (ROOT / "docs/sprints/sprint-1-plan.md").read_text(encoding="utf-8")
    items = []
    for tid, task, who, est in re.findall(r"^\| (T-\d+) \| (.+?) \| (.+?) \| (\d+) \|", text, re.M):
        body = f"Sprint 1 task. Owner: {who}. Estimate: {est} h.\n\nSee docs/sprints/sprint-1-plan.md."
        items.append((f"{tid} · {task}", body, ["task"], MILESTONE))
    return items


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    repo, dry = sys.argv[1], "--dry-run" in sys.argv
    for name, color in LABELS.items():
        gh("label", "create", name, "--color", color, "--force", "--repo", repo, dry=dry)
    try:
        gh("api", f"repos/{repo}/milestones", "-f", f"title={MILESTONE}", dry=dry)
    except subprocess.CalledProcessError:
        pass  # the milestone already exists
    urls = []
    for title, body, labels, milestone in parse_backlog() + parse_tasks():
        args = ["issue", "create", "--repo", repo, "--title", title, "--body", body, "--label", ",".join(labels)]
        if milestone:
            args += ["--milestone", milestone]
        url = gh(*args, dry=dry)
        urls.append(url)
        print(("would create: " if dry else "created: ") + title)
    if dry:
        return
    owner = repo.split("/")[0]
    number = gh("project", "create", "--owner", owner, "--title", BOARD, "--format", "json")
    number = re.search(r'"number":\s*(\d+)', number).group(1)
    for url in urls:
        gh("project", "item-add", number, "--owner", owner, "--url", url)
    print(f"Board '{BOARD}' created with {len(urls)} items. Add the columns Sprint 1, In progress and Review "
          "to the Status field in the web interface, then move the cards.")


if __name__ == "__main__":
    main()
