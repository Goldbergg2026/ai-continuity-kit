#!/usr/bin/env python3
"""Small, dependency-free integrity checks for AI Continuity Kit."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "README.ru.md",
    "SECURITY.md",
    "LICENSE",
    "docs/QUICKSTART.md",
    "docs/CORE_MODEL.md",
    "docs/ARCHITECTURE.md",
    "starter/START.md",
    "starter/AGENTS.md",
    "starter/BOOTSTRAP_PROMPT.md",
    "starter/context/PREFERENCES.md",
    "starter/context/FACTS.md",
    "starter/context/MEMORY.md",
    "starter/projects/example/STATE.md",
    "starter/projects/example/FACTS.md",
    "starter/projects/example/MEMORY.md",
]

# Intentionally narrow: catch obvious credential material without pretending to be
# a complete secret scanner. Keep patterns out of sample content.
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub classic token": re.compile(r"ghp_[A-Za-z0-9]{30,}"),
    "GitHub fine-grained token": re.compile(r"github_pat_[A-Za-z0-9_]{40,}"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{24,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
}

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def check_required(errors: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            errors.append(f"missing required path: {rel}")


def iter_markdown_files():
    for path in ROOT.rglob("*.md"):
        if ".git" not in path.parts:
            yield path


def normalize_link(raw: str) -> str | None:
    target = raw.strip()
    if not target:
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    return unquote(target)


def check_links(errors: list[str]) -> None:
    for md in iter_markdown_files():
        text = md.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = normalize_link(raw)
            if target is None:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"link escapes repository: {md.relative_to(ROOT)} -> {target}")
                continue
            if not candidate.exists():
                errors.append(f"broken relative link: {md.relative_to(ROOT)} -> {target}")


def check_secret_like_material(errors: list[str]) -> None:
    skip = {Path("tools/validate.py")}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        if rel in skip:
            continue
        if path.suffix.lower() not in {".md", ".yml", ".yaml", ".txt", ".json", ".toml"} and path.name not in {"LICENSE", ".gitignore"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label} in {rel}")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_links(errors)
    check_secret_like_material(errors)

    if errors:
        print("VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    md_count = sum(1 for _ in iter_markdown_files())
    print("VALIDATION: PASS")
    print(f"- required paths: {len(REQUIRED_PATHS)} present")
    print(f"- markdown files checked: {md_count}")
    print("- relative links: PASS")
    print("- narrow secret-pattern scan: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
