"""Tests for core.validator."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.validator import validate_name, validate_message, validate_submission


def test_validate_name_empty():
    result = validate_name("")
    assert not result.is_valid
    assert "empty" in result.errors[0].lower()


def test_validate_name_whitespace_only():
    result = validate_name("    ")
    assert not result.is_valid


def test_validate_name_valid():
    result = validate_name("Ada Lovelace")
    assert result.is_valid
    assert result.errors == []


def test_validate_name_too_long():
    result = validate_name("a" * 100)
    assert not result.is_valid
    assert "cannot exceed" in result.errors[0]


def test_validate_message_empty_triggers_warning_not_error():
    result = validate_message("")
    assert result.is_valid  # empty message is a warning, not a hard error
    assert len(result.warnings) == 1
    assert result.errors == []


def test_validate_message_valid():
    result = validate_message("Hello, world!")
    assert result.is_valid
    assert result.warnings == []


def test_validate_message_too_long():
    result = validate_message("a" * 5000)
    assert not result.is_valid
    assert result.errors


def test_validate_submission_combo():
    name_result, message_result = validate_submission("Ada", "Hello!")
    assert name_result.is_valid
    assert message_result.is_valid
