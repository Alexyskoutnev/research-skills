#!/usr/bin/env python3
"""Run the sentence-audit defect list over a LaTeX or Markdown file.

Every check here is one of the mechanical rules from the skills in this repo. The point is that
these are the defects a machine can find, so you never spend a 2am pass hunting for them by eye.

    python3 scripts/audit.py paper.tex
    python3 scripts/audit.py --rules            list every rule and where it comes from
    python3 scripts/audit.py paper.tex --only bare-this,hedge
    python3 scripts/audit.py paper.tex --quiet  exit code only, for CI

Exit code is 1 when anything is flagged, so it drops straight into a pre-commit hook.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# ---------------------------------------------------------------------------
# LaTeX stripping. We audit prose, not markup, so math and code never get flagged.
# ---------------------------------------------------------------------------

_BLANKED = [
    (re.compile(r"(?s)\\begin\{(equation|align|figure|table|lstlisting|verbatim|algorithm)\*?\}.*?"
                r"\\end\{\1\*?\}"), " "),
    (re.compile(r"(?s)\$\$.*?\$\$"), " MATH "),
    (re.compile(r"\$[^$\n]*\$"), " MATH "),
    (re.compile(r"(?s)```.*?```"), " CODE "),
    (re.compile(r"`[^`\n]*`"), " CODE "),
    (re.compile(r"(?m)^\s*%.*$"), " "),
    (re.compile(r"\\(cite|ref|label|eqref|autoref)\{[^}]*\}"), " CITE "),
    (re.compile(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?"), " "),
]


def strip_markup(text: str) -> str:
    for pattern, repl in _BLANKED:
        text = pattern.sub(repl, text)
    return text.replace("{", " ").replace("}", " ")


def sentences(text: str):
    """Yield (sentence, offset). Abbreviations that are not sentence ends are respected."""
    protected = re.sub(r"\b(e\.g|i\.e|et al|cf|vs|Fig|Eq|Sec|Tab|Alg|approx|resp)\.",
                       lambda m: m.group(0).replace(".", "\x00"), text)
    start = 0
    for match in re.finditer(r"[.!?](?=\s|$)", protected):
        end = match.end()
        chunk = protected[start:end].replace("\x00", ".").strip()
        if chunk:
            yield chunk, start
        start = end
    tail = protected[start:].replace("\x00", ".").strip()
    if tail:
        yield tail, start


@dataclass
class Finding:
    line: int
    rule: str
    excerpt: str
    message: str


# ---------------------------------------------------------------------------
# The rules. Each returns a list of (offset, excerpt, message).
# ---------------------------------------------------------------------------

RULE_SOURCES = {
    "bare-this": "sentence-audit: never a bare This/These",
    "hedge": "abstract-writing: no 'can', it concedes the result might not happen",
    "lonely-number": "results-writing: numbers travel in pairs",
    "weak-verb": "abstract-writing: strongest verb available",
    "passive": "results-writing: name the agent",
    "dead-noun": "sentence-audit: categories with no members",
    "long-sentence": "sentence-audit: short sentences, divide and condense",
    "em-dash": "house style: no em dashes",
    "caption-shows": "caption-writing: captions state the claim, not 'This figure shows'",
    "future-work-vague": "conclusion-writing: a refutable vista, not a gesture",
}

_BARE_THIS = re.compile(r"(?<![\w-])(This|These|That|Those)\s+(?=(is|are|was|were|shows?|showed|"
                        r"demonstrates?|means?|meant|suggests?|implies|indicates?|gives?|makes?|"
                        r"allows?|leads?|results?|happens?|follows?|holds?)\b)")
_HEDGE = re.compile(r"(?<![\w-])(can|could|may|might|potentially|possibly|arguably)(?![\w-])", re.I)
_WEAK_VERB = re.compile(r"(?<![\w-])(is able to|serves as|acts as|is designed to|aims to|"
                        r"seeks to|attempts to|works to|helps to|is used to)(?![\w-])", re.I)
_PASSIVE = re.compile(r"(?<![\w-])(was|were|is|are|been|being)\s+(\w+ed|shown|found|seen|given|"
                      r"taken|known|done|made|held|built|drawn)(?![\w-])", re.I)
_DEAD_NOUN = re.compile(r"(?<![\w-])(thing|things|stuff|aspect|aspects|factor|factors|element|"
                        r"elements|issue|issues|area|areas)(?![\w-])", re.I)
_CAPTION_SHOWS = re.compile(r"(?i)\b(this|the)\s+(figure|table|plot|chart|graph)\s+(shows|"
                            r"illustrates|depicts|presents|displays)\b")
_VAGUE_FUTURE = re.compile(r"(?i)\b(future work|we (?:plan|hope|intend) to|in future|"
                           r"further (?:research|work|study))\b")
_NUMBER = re.compile(r"(?<![\w.])(\d+(?:[.,]\d+)?)\s*(%|percent|x|ms|s|GB|MB|K|M|B)?(?![\w])")

MAX_WORDS = 45


def _is_incidental(token: str) -> bool:
    """Small counts and four-digit years are not claims, so they need no comparison."""
    try:
        value = float(token.replace(",", ""))
    except ValueError:
        return True
    if value in (1, 2, 3, 4):
        return True
    return token.isdigit() and len(token) == 4 and 1900 <= value <= 2099


def _flag(pattern, sentence, message, *, only_first=True):
    out = []
    for m in pattern.finditer(sentence):
        out.append((m.start(), m.group(0).strip(), message))
        if only_first:
            break
    return out


def check_sentence(sentence: str, rules: set[str]):
    found = []
    if "bare-this" in rules:
        found += _flag(_BARE_THIS, sentence,
                       "bare demonstrative: name the noun it points at")
    if "hedge" in rules:
        found += _flag(_HEDGE, sentence,
                       "hedge: state what the system does, not what it could do")
    if "weak-verb" in rules:
        found += _flag(_WEAK_VERB, sentence, "weak verb periphrasis: use the verb itself")
    if "passive" in rules:
        found += _flag(_PASSIVE, sentence, "passive with no agent: say who or what did it")
    if "dead-noun" in rules:
        found += _flag(_DEAD_NOUN, sentence, "dead noun: a category with no members")
    if "caption-shows" in rules:
        found += _flag(_CAPTION_SHOWS, sentence,
                       "caption opens by announcing itself: lead with the claim instead")
    if "future-work-vague" in rules:
        for m in _VAGUE_FUTURE.finditer(sentence):
            if not _NUMBER.search(sentence):
                found.append((m.start(), m.group(0),
                              "vague future work: name what would be measured"))
            break
    if "em-dash" in rules and "\u2014" in sentence:
        found.append((sentence.index("\u2014"), "\u2014", "em dash: house style forbids it"))
    if "long-sentence" in rules:
        words = len(sentence.split())
        if words > MAX_WORDS:
            found.append((0, f"[{words} words]",
                          f"sentence runs {words} words: divide it"))
    if "lonely-number" in rules:
        numbers = [m for m in _NUMBER.finditer(sentence)
                   if m.group(2) or not _is_incidental(m.group(1))]
        if len(numbers) == 1 and not re.search(
                r"(?i)\b(versus|vs\.?|against|compared|baseline|from|than|up|down|over)\b", sentence):
            m = numbers[0]
            found.append((m.start(), m.group(0),
                          "lonely number: pair it with what it beats"))
    return found


def audit(path: Path, rules: set[str]) -> list[Finding]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    prose = strip_markup(raw) if path.suffix in {".tex", ".latex"} else raw
    # Offsets survive stripping only if lengths match, so recompute line numbers from the
    # stripped text and accept that they track the stripped copy for .tex input.
    findings = []
    for sentence, offset in sentences(prose):
        line = prose.count("\n", 0, offset) + 1
        for local, excerpt, message in check_sentence(sentence, rules):
            findings.append(Finding(line, _rule_for(message), excerpt, message))
    return findings


def _rule_for(message: str) -> str:
    table = {
        "bare demonstrative": "bare-this", "hedge:": "hedge", "weak verb": "weak-verb",
        "passive with": "passive", "dead noun": "dead-noun", "caption opens": "caption-shows",
        "vague future": "future-work-vague", "em dash": "em-dash",
        "sentence runs": "long-sentence", "lonely number": "lonely-number",
    }
    for key, rule in table.items():
        if message.startswith(key):
            return rule
    return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--only", help="comma-separated rule names")
    parser.add_argument("--rules", action="store_true", help="list the rules and exit")
    parser.add_argument("--quiet", action="store_true", help="exit code only")
    args = parser.parse_args()

    if args.rules:
        width = max(len(r) for r in RULE_SOURCES)
        for rule, source in RULE_SOURCES.items():
            print(f"  {rule:<{width}}  {source}")
        return 0

    if not args.files:
        parser.error("give at least one file, or --rules")

    rules = set(RULE_SOURCES)
    if args.only:
        asked = {r.strip() for r in args.only.split(",")}
        unknown = asked - rules
        if unknown:
            parser.error(f"unknown rule(s): {', '.join(sorted(unknown))}")
        rules = asked

    total = 0
    for path in args.files:
        if not path.exists():
            print(f"{path}: no such file", file=sys.stderr)
            return 2
        findings = audit(path, rules)
        total += len(findings)
        if args.quiet:
            continue
        if not findings:
            print(f"{path}: clean")
            continue
        print(f"\n{path}: {len(findings)} flagged\n")
        for f in findings:
            print(f"  {path}:{f.line}  [{f.rule}]")
            print(f"      {f.excerpt}")
            print(f"      {f.message}")
    if not args.quiet and total:
        print(f"\n{total} total. None of these are style opinions. Each one is a rule from a "
              f"SKILL.md in this repo, and `--rules` says which.")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
