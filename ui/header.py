"""
header.py
Renders the compact hero section and instruction banner.
"""

from __future__ import annotations

import streamlit as st

from utils.constants import APP_ICON, APP_NAME, APP_TAGLINE
from utils.theme import render_html_markup


def render_header() -> None:
    """Render compact hero header."""

    render_html_markup(
        f"""<div class="hero">
<div class="hero-icon">{APP_ICON}</div>
<h1 class="hero-title">{APP_NAME}</h1>
<p class="hero-tagline">{APP_TAGLINE}</p>
</div>""",
        height=140,
    )

    render_html_markup(
        """<div class="instructions-card">
<span class="instructions-label">Instructions</span>
<p>
Enter your <strong>Name</strong> and <strong>Message</strong>,
then click <strong>Transmit</strong>.
</p>
</div>""",
        height=120,
    )