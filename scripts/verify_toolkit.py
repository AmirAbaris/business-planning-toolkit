#!/usr/bin/env python3
"""Check the vendored snapshot without executing any vendored code or networking."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote


def verify(root):
    errors = []
    lock = json.loads((root / "upstream-lock.json").read_text())
    expected = set()
    skills_root = root / ".agents/skills"
    for skill in lock["skills"]:
        folder = root / skill["destination"]
        if not re.fullmatch(r"[0-9a-f]{40}", skill["commit"]):
            errors.append(f"Invalid commit: {skill['name']}")
        entry = folder / "SKILL.md"
        if not entry.is_file():
            errors.append(f"Missing entrypoint: {entry}")
        else:
            text = entry.read_text()
            if not text.startswith("---\n") or "\n---\n" not in text[4:]:
                errors.append(f"Missing frontmatter: {entry}")
            else:
                front = text.split("---", 2)[1]
                if not re.search(r"^name: " + re.escape(skill["name"]) + r"$", front, re.M):
                    errors.append(f"Name mismatch: {entry}")
                if not re.search(r"^description: .+", front, re.M):
                    errors.append(f"Missing description: {entry}")
        for rel, digest in skill["sha256"].items():
            path = root / rel
            expected.add(path)
            if not path.resolve().is_relative_to(root.resolve()):
                errors.append(f"Path escapes repository: {rel}")
            elif path.is_symlink() or not path.is_file():
                errors.append(f"Missing or linked file: {rel}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append(f"Snapshot changed: {rel}")
        if not (folder / "LICENSE").is_file():
            errors.append(f"Missing license: {folder}")
    actual = {p for p in skills_root.rglob("*") if p.is_file()
              and "__pycache__" not in p.parts and p.suffix != ".pyc"}
    for extra in sorted(actual - expected):
        errors.append(f"Unreviewed vendor file: {extra.relative_to(root)}")
    for path in sorted(actual):
        if path.suffix != ".md":
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            if ":" in target or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            if target and not (path.parent / target).exists():
                errors.append(f"Broken reference in {path.relative_to(root)}: {target}")
    for required in ("AGENTS.md", "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md",
                     "docs-toolkit/UPSTREAM-REVIEW.md"):
        if not (root / required).is_file():
            errors.append(f"Missing toolkit file: {required}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Verified {len(lock['skills'])} skills and {len(expected)} vendored files; local references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(verify(Path(__file__).resolve().parents[1]))
