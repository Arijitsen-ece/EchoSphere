"""
formatter.py
Formats the success message and other user-facing text blocks using
f-strings, as required by the assignment spec.
"""

from __future__ import annotations


def format_transmission_success(name: str, message: str) -> str:
    """
    Build the transmission-success message using an f-string, exactly
    matching the assignment's required copy:

        Transmission successful!
        Greetings, {Name}
        We received your message: {Message}
    """
    clean_name = name.strip()
    clean_message = message.strip()
    return (
        f"**Transmission successful!**\n\n"
        f"Greetings, **{clean_name}**\n\n"
        f"We received your message:\n\n> {clean_message}"
    )


def format_reading_time(words: int, wpm: int = 200) -> str:
    """Return a human-readable estimated reading time string."""
    minutes = words / wpm if wpm > 0 else 0
    if minutes < 1:
        seconds = max(1, round(minutes * 60))
        return f"{seconds} sec read"
    return f"{max(1, round(minutes))} min read"
