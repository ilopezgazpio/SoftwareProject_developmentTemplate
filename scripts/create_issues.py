"""Create labels, milestone, issues and the project board on GitHub from the backlog files.

Run after the repository exists on GitHub and `gh auth login` is done. The board needs the
project scope on the token: `gh auth refresh -s project,read:project`.

    python scripts/create_issues.py OWNER/REPO            # create what is missing
    python scripts/create_issues.py OWNER/REPO --dry-run  # only print what would be created

Safe to run again: issues whose title already exists are skipped, and an existing board is reused.
Sources: docs/backlog/product-backlog.md (epics and stories) and docs/sprints/sprint-1-plan.md (tasks).
"""

import json
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


def gh(*args, dry=False, ok_to_fail=False):
    cmd = ["gh", *args]
    if dry:
        print("  $", " ".join(a if " " not in a else repr(a) for a in cmd)[:160])
        return ""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 and not ok_to_fail:
        sys.exit(f"gh failed: {' '.join(cmd[:3])} ...\n{result.stderr.strip()}")
    return result.stdout.strip()


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


def existing_issues(repo):
    out = gh("issue", "list", "--repo", repo, "--state", "all", "--limit", "200", "--json", "title,url")
    return {i["title"]: i["url"] for i in json.loads(out or "[]")}


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    repo, dry = sys.argv[1], "--dry-run" in sys.argv
    owner = repo.split("/")[0]

    for name, color in LABELS.items():
        gh("label", "create", name, "--color", color, "--force", "--repo", repo, dry=dry)
    gh("api", f"repos/{repo}/milestones", "-f", f"title={MILESTONE}", dry=dry, ok_to_fail=True)

    have = {} if dry else existing_issues(repo)
    urls = []
    for title, body, labels, milestone in parse_backlog() + parse_tasks():
        if title in have:
            print("exists:  " + title)
            urls.append(have[title])
            continue
        args = ["issue", "create", "--repo", repo, "--title", title, "--body", body, "--label", ",".join(labels)]
        if milestone:
            args += ["--milestone", milestone]
        urls.append(gh(*args, dry=dry))
        print(("would create: " if dry else "created: ") + title)
    if dry:
        return

    boards = gh("project", "list", "--owner", owner, "--format", "json", ok_to_fail=True)
    if not boards:
        sys.exit("The board needs the project scope on your token. Run\n"
                 "    gh auth refresh -s project,read:project\n"
                 "and then this script again: the issues above are kept, not duplicated.")
    number = next((p["number"] for p in json.loads(boards)["projects"] if p["title"] == BOARD), None)
    if number is None:
        created = gh("project", "create", "--owner", owner, "--title", BOARD, "--format", "json")
        number = json.loads(created)["number"]
        print(f"created board: {BOARD}")
    else:
        print(f"exists board: {BOARD}")
    for url in urls:
        gh("project", "item-add", str(number), "--owner", owner, "--url", url, ok_to_fail=True)
    print(f"{len(urls)} items on the board. In the web interface add the columns Sprint 1, In progress and "
          "Review to the Status field, then move the cards as in docs/board/README.md.")


if __name__ == "__main__":
    main()
