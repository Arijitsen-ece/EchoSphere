"""
helpers.py
Small, generic, stateless helper functions used across the app.

These are intentionally free of Streamlit imports so they can be
unit-tested in isolation (see tests/).
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any


def now_iso() -> str:
    """Return the current UTC timestamp in ISO-8601 format."""
    return datetime.now(timezone.utc).isoformat()


def safe_read_json(path: str, default: Any) -> Any:
    """
    Read a JSON file safely, returning `default` if the file is missing,
    empty, or malformed. Never raises for expected failure modes.
    """
    try:
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            return default
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default


def safe_write_json(path: str, data: Any) -> bool:
    """
    Write `data` to `path` as JSON, creating parent directories if needed.
    Returns True on success, False on failure (never raises).
    """
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except OSError:
        return False


def truncate(text: str, max_len: int, suffix: str = "…") -> str:
    """Truncate `text` to `max_len` characters, appending `suffix` if cut."""
    if len(text) <= max_len:
        return text
    return text[: max(0, max_len - len(suffix))] + suffix


def pluralize(count: int, singular: str, plural: str | None = None) -> str:
    """Return `singular` or `plural` (default singular + 's') based on count."""
    if count == 1:
        return singular
    return plural if plural is not None else f"{singular}s"
