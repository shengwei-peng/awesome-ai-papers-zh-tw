"""Fail when the translator (shengwei-peng/ai-paper-translator) is missing Hugging Face daily papers.

The translator runs daily at 04:30 Asia/Taipei and re-sweeps the two previous days, so:
- the day SETTLED_LAG_DAYS ago is final and must be fully translated (up to MAX_MISSING papers);
- yesterday must have at least one translated paper, otherwise the translator did not run at all.

Usage: python3 check_coverage.py [YYYY-MM-DD]   (a date checks only that day, as settled)
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Callable

HF_API = "https://huggingface.co/api/daily_papers"
PAGE_SIZE = 100  # API maximum
MAX_PAGES = 10
SETTLED_LAG_DAYS = 3
NOT_OPEN_YET = "must be less than or equal to"
PAPERS_DIR = Path(__file__).resolve().parents[2] / "papers"


def _fetch_page(day: date, page: int) -> list[dict]:
    url = f"{HF_API}?date={day.isoformat()}&limit={PAGE_SIZE}&p={page}"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        # HF rejects dates past its newest daily list, which can lag the UTC day
        if e.code == 400 and NOT_OPEN_YET in e.read().decode(errors="replace"):
            return []
        raise


def hf_ids(day: date) -> list[str]:
    ids: list[str] = []
    for page in range(MAX_PAGES):
        fresh = [i for i in (item["paper"]["id"] for item in _fetch_page(day, page)) if i not in ids]
        if not fresh:  # empty page, or HF ignored the page parameter
            break
        ids += fresh
    return ids


def translated_ids(papers_dir: Path) -> set[str]:
    return {path.name.split("_", 1)[0] for path in papers_dir.glob("*.md")}


def check(
    today: date,
    fetch: Callable[[date], list[str]],
    translated: set[str],
    max_missing: int,
    only: date | None = None,
) -> list[str]:
    """Return human-readable problems; empty means healthy."""
    problems = []

    settled = only or today - timedelta(days=SETTLED_LAG_DAYS)
    ids = fetch(settled)
    missing = [i for i in ids if i not in translated]
    print(f"{settled}: {len(ids) - len(missing)}/{len(ids)} translated")
    if len(missing) > max_missing:
        problems.append(f"{settled}: {len(missing)}/{len(ids)} papers not translated: {', '.join(missing)}")

    if only is None:
        yesterday = today - timedelta(days=1)
        ids = fetch(yesterday)
        done = sum(1 for i in ids if i in translated)
        print(f"{yesterday}: {done}/{len(ids)} translated so far")
        if ids and done == 0:
            problems.append(f"{yesterday}: none of {len(ids)} papers translated — did the translator run?")

    return problems


def main(argv: list[str]) -> int:
    only = date.fromisoformat(argv[1]) if len(argv) > 1 and argv[1] else None
    max_missing = int(os.environ.get("MAX_MISSING", "0"))
    today = datetime.now(timezone.utc).date()

    problems = check(today, hf_ids, translated_ids(PAPERS_DIR), max_missing, only)

    for problem in problems:
        print(f"::error::{problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
