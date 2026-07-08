"""Tests for core.processor."""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.processor import process_transmission, save_to_history, load_history


def test_process_transmission_success():
    result = process_transmission("Ada", "Hello, world!")
    assert result.success
    assert result.name_result.is_valid
    assert result.message_result.is_valid
    assert result.metrics is not None
    assert result.history_entry["name"] == "Ada"


def test_process_transmission_empty_name_fails():
    result = process_transmission("", "Hello!")
    assert not result.success
    assert result.name_result.errors


def test_process_transmission_empty_message_warns():
    result = process_transmission("Ada", "")
    assert not result.success
    assert result.message_result.warnings


def test_save_and_load_history_roundtrip():
    with tempfile.TemporaryDirectory() as tmp_dir:
        path = str(Path(tmp_dir) / "history.json")
        entry = {"name": "Ada", "message": "Hi", "estimated_tokens": 1}

        assert save_to_history(entry, path=path) is True
        history = load_history(path=path)

        assert len(history) == 1
        assert history[0]["name"] == "Ada"


def test_save_to_history_ignores_empty_entry():
    with tempfile.TemporaryDirectory() as tmp_dir:
        path = str(Path(tmp_dir) / "history.json")
        assert save_to_history({}, path=path) is False
