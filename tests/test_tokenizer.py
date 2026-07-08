"""Tests for core.tokenizer."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.tokenizer import (
    count_characters,
    count_words,
    estimate_tokens,
    context_usage_percent,
    analyze_text,
)


def test_count_characters():
    assert count_characters("hello") == 5
    assert count_characters("") == 0


def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("   ") == 0
    assert count_words("") == 0


def test_estimate_tokens_basic():
    # 8 characters / 4 chars-per-token = 2 tokens
    assert estimate_tokens("abcdefgh") == 2


def test_estimate_tokens_rounds_up():
    # 5 characters / 4 -> should round up to 2 tokens
    assert estimate_tokens("abcde") == 2


def test_estimate_tokens_empty_string():
    assert estimate_tokens("") == 0


def test_estimate_tokens_invalid_divisor():
    try:
        estimate_tokens("abc", chars_per_token=0)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_context_usage_percent():
    assert context_usage_percent(400, context_window=8000) == 5.0


def test_analyze_text_bundle():
    stats = analyze_text("hello world")
    assert stats.characters == 11
    assert stats.words == 2
    assert stats.estimated_tokens == 3  # ceil(11/4)
    assert stats.context_usage_percent > 0
