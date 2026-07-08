"""
tokenizer.py
Lightweight, dependency-free text-metric calculations: character count,
word count, and an estimated LLM token count using the common
"~4 characters per token" heuristic.
"""

from __future__ import annotations

from dataclasses import dataclass

from utils.constants import ASSUMED_CONTEXT_WINDOW, CHARS_PER_TOKEN


@dataclass
class TokenStats:
    """Container for computed text statistics."""

    characters: int
    words: int
    estimated_tokens: int
    context_usage_percent: float


def count_characters(text: str) -> int:
    """Return the raw character count of `text` (including whitespace)."""
    return len(text)


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in `text`."""
    return len(text.split())


def estimate_tokens(text: str, chars_per_token: float = CHARS_PER_TOKEN) -> int:
    """
    Estimate the number of LLM tokens in `text` using the heuristic:
        tokens ≈ characters / chars_per_token

    Rounded up, since a partial token still consumes a full token slot.
    """
    if chars_per_token <= 0:
        raise ValueError("chars_per_token must be greater than zero.")
    characters = count_characters(text)
    return int((characters + chars_per_token - 1) // chars_per_token) if characters else 0


def context_usage_percent(
    estimated_token_count: int, context_window: int = ASSUMED_CONTEXT_WINDOW
) -> float:
    """Return what percentage of an assumed context window is consumed."""
    if context_window <= 0:
        raise ValueError("context_window must be greater than zero.")
    return round((estimated_token_count / context_window) * 100, 2)


def analyze_text(text: str) -> TokenStats:
    """Run all metrics on `text` and return a single TokenStats object."""
    characters = count_characters(text)
    words = count_words(text)
    tokens = estimate_tokens(text)
    usage = context_usage_percent(tokens)
    return TokenStats(
        characters=characters,
        words=words,
        estimated_tokens=tokens,
        context_usage_percent=usage,
    )
