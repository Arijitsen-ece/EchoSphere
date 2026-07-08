"""
cards.py
Compact glassmorphism metric cards for EchoSphere.

Optimized for a single-screen dashboard layout while preserving
all assignment functionality.
"""

from __future__ import annotations

import streamlit as st

from core.tokenizer import TokenStats
from utils.constants import ASSUMED_CONTEXT_WINDOW
from utils.theme import render_html_markup


def render_metric_card(
    label: str,
    value: str,
    icon: str,
    accent: str = "primary",
) -> None:
    """
    Render a compact metric card.
    """

    render_html_markup(
        f"""
        <div class="metric-card accent-{accent}">
            <div class="metric-icon">{icon}</div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-label">
                {label}
            </div>

        </div>
        """,
        height=120,
    )


def render_system_check(
    stats: TokenStats,
    reading_time: str,
) -> None:
    """
    Render the compact System Check panel.

    Displays:
        • Characters
        • Words
        • Estimated Tokens
        • Reading Time
        • Context Usage
    """

    # -------------------------------------------------------
    # Compact heading
    # -------------------------------------------------------

    st.markdown("### 🧪 System Check")

    # -------------------------------------------------------
    # Metric Cards
    # -------------------------------------------------------

    col1, col2, col3, col4 = st.columns(
        4,
        gap="small",
    )

    with col1:
        render_metric_card(
            "Characters",
            f"{stats.characters:,}",
            "🔤",
            "primary",
        )

    with col2:
        render_metric_card(
            "Words",
            f"{stats.words:,}",
            "📝",
            "secondary",
        )

    with col3:
        render_metric_card(
            "Tokens",
            f"{stats.estimated_tokens:,}",
            "🧮",
            "success",
        )

    with col4:
        render_metric_card(
            "Read",
            reading_time,
            "⏱️",
            "warning",
        )

    # -------------------------------------------------------
    # Context Usage
    # -------------------------------------------------------

    usage = min(
        100,
        stats.context_usage_percent,
    )

    render_html_markup(
        f"""
        <div style="
            margin-top:0.6rem;
            margin-bottom:0.25rem;
            font-size:0.90rem;
            color:#C9D1D9;
            font-weight:600;
        ">
            Context Usage:
            <span style="color:#4F8CFF;">
                {stats.estimated_tokens:,}
            </span>
            /
            {ASSUMED_CONTEXT_WINDOW:,}
            tokens
            ({usage:.2f}%)
        </div>
        """,
        height=80,
    )

    st.progress(
        usage / 100,
        text=None,
    )

    # -------------------------------------------------------
    # Compact Information
    # -------------------------------------------------------

    st.caption(
        "Estimated using the standard approximation of "
        "1 token ≈ 4 characters."
    )