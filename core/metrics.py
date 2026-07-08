"""
metrics.py
Derived, higher-level metrics that build on core.tokenizer's raw
counts (e.g. estimated reading time). Kept separate from tokenizer.py
so each module has a single, clear responsibility.
"""

from __future__ import annotations

from dataclasses import dataclass

from core.tokenizer import TokenStats, analyze_text
from core.formatter import format_reading_time
from utils.constants import AVERAGE_READING_WPM


@dataclass
class MessageMetrics:
    """Full metrics bundle for a submitted message."""

    stats: TokenStats
    reading_time: str


def compute_message_metrics(message: str, wpm: int = AVERAGE_READING_WPM) -> MessageMetrics:
    """Compute the full metrics bundle (counts + reading time) for a message."""
    stats = analyze_text(message)
    reading_time = format_reading_time(stats.words, wpm)
    return MessageMetrics(stats=stats, reading_time=reading_time)
