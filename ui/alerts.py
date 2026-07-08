"""
alerts.py
Thin wrappers around Streamlit's native alert components so that
validation messaging stays consistent and centrally controlled.
"""

from __future__ import annotations

import streamlit as st

from core.formatter import format_transmission_success


def show_name_errors(errors: list[str]) -> None:
    """Display each name-validation error using st.error()."""
    for error in errors:
        st.error(f"🚫 {error}")


def show_message_warnings(warnings: list[str]) -> None:
    """Display each message-validation warning using st.warning()."""
    for warning in warnings:
        st.warning(f"⚠️ {warning}")


def show_message_errors(errors: list[str]) -> None:
    """Display each message-validation error using st.error()."""
    for error in errors:
        st.error(f"🚫 {error}")


def show_transmission_success(name: str, message: str) -> None:
    """Display the final success card using st.success()."""
    st.success(format_transmission_success(name, message))
    st.balloons()
