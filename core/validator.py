"""
validator.py
All input-validation logic for EchoSphere lives here, decoupled from
Streamlit so it can be unit-tested directly.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from utils.constants import (
    MAX_MESSAGE_LENGTH,
    MAX_NAME_LENGTH,
    MIN_MESSAGE_LENGTH,
    MIN_NAME_LENGTH,
)


@dataclass
class ValidationResult:
    """Structured result of a validation pass."""

    is_valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def validate_name(name: str) -> ValidationResult:
    """
    Validate the 'Name' field.

    Rules:
      - Must not be empty after trimming whitespace -> error
      - Must not exceed MAX_NAME_LENGTH -> error
    """
    errors: list[str] = []
    trimmed = name.strip()

    if len(trimmed) < MIN_NAME_LENGTH:
        errors.append("Name cannot be empty.")
    elif len(trimmed) > MAX_NAME_LENGTH:
        errors.append(f"Name cannot exceed {MAX_NAME_LENGTH} characters.")

    return ValidationResult(is_valid=len(errors) == 0, errors=errors)


def validate_message(message: str) -> ValidationResult:
    """
    Validate the 'Message' field.

    Rules:
      - Must not be empty after trimming whitespace -> warning
        (per assignment spec: empty message triggers st.warning, not st.error)
      - Must not exceed MAX_MESSAGE_LENGTH -> error
    """
    errors: list[str] = []
    warnings: list[str] = []
    trimmed = message.strip()

    if len(trimmed) < MIN_MESSAGE_LENGTH:
        warnings.append("Message is empty. Please enter a message before transmitting.")
    elif len(trimmed) > MAX_MESSAGE_LENGTH:
        errors.append(f"Message cannot exceed {MAX_MESSAGE_LENGTH} characters.")

    return ValidationResult(is_valid=len(errors) == 0, errors=errors, warnings=warnings)


def validate_submission(name: str, message: str) -> tuple[ValidationResult, ValidationResult]:
    """Convenience wrapper validating both fields at once."""
    return validate_name(name), validate_message(message)
