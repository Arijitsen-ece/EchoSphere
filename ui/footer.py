"""
footer.py
Compact professional footer for EchoSphere.

Optimized for a clean, single-viewport layout.
"""

from __future__ import annotations

import streamlit as st

from utils.constants import APP_NAME, APP_VERSION
from utils.theme import render_html_markup


def render_footer() -> None:
    """Render a compact footer."""

    render_html_markup(
        f"""
        <div class="footer">
            © 2026 <strong>{APP_NAME}</strong> • Version {APP_VERSION} • Built with 💙 using Streamlit
        </div>
        """,
        height=80,
    )