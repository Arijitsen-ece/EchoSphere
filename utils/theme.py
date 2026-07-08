"""
theme.py
Handles Streamlit page configuration and CSS injection so that
app.py stays declarative and free of styling clutter.
"""

from __future__ import annotations

import os

import streamlit as st
import streamlit.components.v1 as components

from utils.constants import APP_NAME, APP_ICON


def configure_page() -> None:
    """Set page-wide Streamlit configuration. Must be the first st.* call."""
    st.set_page_config(
        page_title=f"{APP_NAME} · Message Transmission Interface",
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )


def inject_css(css_path: str = "assets/styles.css") -> None:
    """
    Load and inject the custom stylesheet. Fails silently (with a subtle
    warning) if the file is missing, so the app still renders with
    Streamlit's default theme rather than crashing.
    """
    if not os.path.exists(css_path):
        st.warning(f"Stylesheet not found at '{css_path}'. Using default theme.")
        return

    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def render_html_markup(html: str, *, height: int = 140) -> None:
    """Render custom HTML markup reliably inside Streamlit."""
    css_path = "assets/styles.css"
    css = ""

    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css = f.read()

    components.html(f"<style>{css}</style>{html}", height=height, scrolling=False)
