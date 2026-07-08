"""
app.py
EchoSphere — Professional Message Transmission Interface.

This is the thin orchestration layer: it wires together the `core`
(business logic), `ui` (presentation), and `utils` (shared helpers)
packages. All heavy lifting happens in those modules, keeping this
file short, readable, and easy to reason about.
"""

from __future__ import annotations

import streamlit as st

from core.processor import process_transmission, save_to_history
from ui.alerts import (
    show_message_warnings,
    show_message_errors,
    show_name_errors,
    show_transmission_success,
)
from ui.cards import render_system_check
from ui.footer import render_footer
from ui.header import render_header
from ui.preview import render_message_preview
from ui.sidebar import render_sidebar
from utils.constants import MAX_MESSAGE_LENGTH, MAX_NAME_LENGTH
from utils.theme import configure_page, inject_css, render_html_markup


def _init_session_state() -> None:
    """Initialize session-state flags used to prevent duplicate submissions."""
    if "is_submitting" not in st.session_state:
        st.session_state.is_submitting = False
    if "last_result" not in st.session_state:
        st.session_state.last_result = None


def render_transmission_form() -> tuple[str, str, bool]:
    """Render the name/message inputs and the Transmit button."""
    name = st.text_input(
        "Name",
        max_chars=MAX_NAME_LENGTH,
        placeholder="e.g. Ada Lovelace",
        help=f"Up to {MAX_NAME_LENGTH} characters.",
    )
    message = st.text_area(
        "Message",
        max_chars=MAX_MESSAGE_LENGTH,
        placeholder="Type the message you'd like to transmit…",
        height=110,
        help=f"Up to {MAX_MESSAGE_LENGTH} characters.",
    )

    render_message_preview(name, message)

    transmit_clicked = st.button(
        "🚀 Transmit",
        use_container_width=True,
        disabled=st.session_state.is_submitting,
    )
    return name, message, transmit_clicked


def handle_transmission(name: str, message: str) -> None:
    """
    Run the full transmission pipeline: validate -> show alerts ->
    compute metrics -> show success + system check -> persist history.

    Guards against multiple rapid submissions using a session-state
    lock, and wraps processing in a try/except for graceful handling
    of any unexpected runtime errors.
    """
    st.session_state.is_submitting = True
    try:
        result = process_transmission(name, message)

        if result.name_result.errors:
            show_name_errors(result.name_result.errors)
        if result.message_result.warnings:
            show_message_warnings(result.message_result.warnings)
        if result.message_result.errors:
            show_message_errors(result.message_result.errors)

        if result.success and result.metrics is not None:
            show_transmission_success(name, message)
            render_system_check(result.metrics.stats, result.metrics.reading_time)
            save_to_history(result.history_entry)

        st.session_state.last_result = result
    except Exception as exc:  # noqa: BLE001 — top-level guard for a graceful UX
        st.error(f"⚠️ An unexpected error occurred while processing your transmission: {exc}")
    finally:
        st.session_state.is_submitting = False


def main() -> None:
    """Application entry point."""
    configure_page()
    inject_css()
    _init_session_state()

    render_sidebar()
    render_header()

    left, right = st.columns([1.45, 1], gap="medium")
    with left:
        name, message, transmit_clicked = render_transmission_form()

    with right:
        if transmit_clicked:
            handle_transmission(name, message)
        elif st.session_state.last_result is None:
            render_html_markup(
                """
                <div class="preview-card compact-card">
                    <div class="preview-header">
                        <span class="preview-dot"></span>
                        <span>Awaiting Transmission</span>
                    </div>
                    <div class="preview-body">
                        Ready to receive your message.
                    </div>
                </div>
                """,
                height=120,
            )
    

    render_footer()


if __name__ == "__main__":
    main()
