"""
processor.py
Orchestration layer that ties validation, metrics, and persistence
together for a single "transmission" submission. This is the one
place app.py needs to call into for the core business logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from core.metrics import MessageMetrics, compute_message_metrics
from core.validator import ValidationResult, validate_submission
from utils.constants import HISTORY_FILE_PATH, MAX_HISTORY_ENTRIES
from utils.helpers import now_iso, safe_read_json, safe_write_json


@dataclass
class TransmissionResult:
    """Full result of processing a single transmission attempt."""

    success: bool
    name_result: ValidationResult
    message_result: ValidationResult
    metrics: MessageMetrics | None = None
    history_entry: dict = field(default_factory=dict)


def process_transmission(name: str, message: str) -> TransmissionResult:
    """
    Validate the submitted name/message, and if both pass, compute
    metrics and build a history entry. Does NOT persist to disk itself
    (see save_to_history) so the caller can decide whether/when to save.
    """
    name_result, message_result = validate_submission(name, message)
    success = name_result.is_valid and message_result.is_valid and not message_result.warnings

    metrics = compute_message_metrics(message) if message.strip() else None

    entry: dict = {}
    if success and metrics is not None:
        entry = {
            "timestamp": now_iso(),
            "name": name.strip(),
            "message": message.strip(),
            "characters": metrics.stats.characters,
            "words": metrics.stats.words,
            "estimated_tokens": metrics.stats.estimated_tokens,
        }

    return TransmissionResult(
        success=success,
        name_result=name_result,
        message_result=message_result,
        metrics=metrics,
        history_entry=entry,
    )


def save_to_history(entry: dict, path: str = HISTORY_FILE_PATH) -> bool:
    """Append a transmission entry to the JSON history log on disk."""
    if not entry:
        return False
    history = safe_read_json(path, default=[])
    if not isinstance(history, list):
        history = []
    history.append(entry)
    # Keep only the most recent N entries to prevent unbounded growth.
    history = history[-MAX_HISTORY_ENTRIES:]
    return safe_write_json(path, history)


def load_history(path: str = HISTORY_FILE_PATH) -> list[dict]:
    """Load transmission history from disk, returning [] if unavailable."""
    history = safe_read_json(path, default=[])
    return history if isinstance(history, list) else []
