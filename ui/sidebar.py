"""
sidebar.py
Compact professional sidebar optimized for a single-screen layout.
"""

from __future__ import annotations

import os

import streamlit as st

from core.processor import load_history
from utils.constants import APP_NAME, APP_TAGLINE
from utils.theme import render_html_markup


def render_sidebar() -> None:
    """Render a compact sidebar."""

    with st.sidebar:

        # ------------------------------------------------------------------
        # Logo
        # ------------------------------------------------------------------
        logo_path = "assets/logo.png"

        if os.path.exists(logo_path):
            st.image(logo_path, width=110)
        else:
            render_html_markup(
                "<div class='sidebar-logo-fallback'>🛰️ EchoSphere</div>",
                height=70,
            )

        # ------------------------------------------------------------------
        # App Name
        # ------------------------------------------------------------------
        st.markdown(f"### {APP_NAME}")
        st.caption(APP_TAGLINE)

        st.markdown("---")

        # ------------------------------------------------------------------
        # Session Statistics
        # ------------------------------------------------------------------
        st.markdown("#### 📊 Session Stats")

        history = load_history()

        total_transmissions = len(history)
        total_tokens = sum(
            item.get("estimated_tokens", 0)
            for item in history
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Sent",
                total_transmissions,
            )

        with col2:
            st.metric(
                "Tokens",
                total_tokens,
            )

        st.markdown("---")

        # ------------------------------------------------------------------
        # About
        # ------------------------------------------------------------------
        st.markdown("#### ℹ About")

        st.caption(
            "Professional message transmission interface "
            "built with Streamlit."
        )

        st.markdown("---")

        # ------------------------------------------------------------------
        # Footer
        # ------------------------------------------------------------------
        st.caption("💙 Streamlit • v1.0")