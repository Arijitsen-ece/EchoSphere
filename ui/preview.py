"""
preview.py
Renders a live "Message Preview" card as the user types, before
transmission — part of the polished SaaS-dashboard feel.
"""

from __future__ import annotations

import streamlit as st

from utils.helpers import truncate
from utils.theme import render_html_markup


def render_message_preview(name: str, message: str) -> None:
    """Render a live preview card of what will be transmitted."""
    display_name = name.strip() or "—"
    display_message = truncate(message.strip(), 240) or "Your message will appear here…"

    render_html_markup(
        f"""
        <div class="preview-card">
            <div class="preview-header">
                <span class="preview-dot"></span>
                <span>Live Preview</span>
            </div>
            <div class="preview-body">
                <p><span class="preview-key">From:</span> {display_name}</p>
                <p><span class="preview-key">Message:</span> {display_message}</p>
            </div>
        </div>
        """,
        height=140,
    )
