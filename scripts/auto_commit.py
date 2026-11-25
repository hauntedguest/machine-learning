#!/usr/bin/env python3
"""Auto-commit and push changes in this repo with descriptive commit messages.

Run by launchd every few minutes (see scripts/install_autocommit.sh).
Safe to run by hand:  python3 scripts/auto_commit.py [--no-push]
"""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


def notebook_summary(text):
    """Return (n_code, n_md, first_md_heading) for notebook JSON text, or None."""
    try:
        nb = json.loads(text)
    except Exception:
        return None
    cells = nb.get("cells", [])
    code = sum(c.get("cell_type") == "code" for c in cells)
    md = sum(c.get("cell_type") == "markdown" for c in cells)
    return code, md


def describe(status, path):
    name = Path(path).name
    verb = {"A": "Add", "M": "Update", "D": "Remove", "R": "Rename"}.get(status, "Update")
    detail = ""
    if path.endswith(".ipynb"):
        new = (REPO / path).read_text() if (REPO / path).exists() else None
        old = git("show", f"HEAD:{path}", check=False) if status != "A" else None
        n_new = notebook_summary(new) if new else None
        n_old = notebook_summary(old) if old else None
        if n_new and n_old:
            dc, dm = n_new[0] - n_old[0], n_new[1] - n_old[1]
            parts = []
            if dc: parts.append(f"{dc:+d} code cells")
            if dm: parts.append(f"{dm:+d} markdown cells")
            detail = f" ({', '.join(parts)})" if parts else " (edited cells/outputs)"
        elif n_new:
            detail = f" ({n_new[0]} code, {n_new[1]} markdown cells)"
        return f"{verb} notebook {name}{detail}"
    if path.endswith(".csv"):
        return f"{verb} dataset {name}"
    if path.endswith(".py"):
        return f"{verb} script {name}"
    return f"{verb} {name}"


def main():
    push = "--no-push" not in sys.argv
    git("add", "-A")
    changes = []
    for line in git("diff", "--cached", "--name-status", "-M").splitlines():
        parts = line.split("\t")
        status, path = parts[0][0], parts[-1]
        changes.append((status, path))

    if changes:
        descs = [describe(s, p) for s, p in changes]
        if len(descs) == 1:
            subject = descs[0]
        else:
            subject = f"{descs[0]} and {len(descs) - 1} other change{'s' if len(descs) > 2 else ''}"
        body = "\n".join(f"- {d}" for d in descs)
        stat = git("diff", "--cached", "--shortstat").strip()
        msg = f"{subject}\n\n{body}\n\n{stat}\n(auto-commit {datetime.now():%Y-%m-%d %H:%M})"
        git("commit", "-q", "-m", msg)
        print(f"Committed: {subject}")
    else:
        print("Nothing to commit.")

    if push:
        # push also retries any earlier commit that failed to push (e.g. offline)
        ahead = git("rev-list", "--count", "@{u}..HEAD", check=False).strip()
        if ahead not in ("", "0"):
            git("push", "-q")
            print("Pushed.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[{datetime.now():%F %T}] ERROR: {e}", file=sys.stderr)
        sys.exit(1)
