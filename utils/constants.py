"""
constants.py
Centralized configuration values for EchoSphere.

Keeping all application constants in one place makes the project
easy to maintain and avoids hardcoded values throughout the codebase.
"""

from __future__ import annotations

# =============================================================================
# Application Metadata
# =============================================================================

APP_NAME: str = "EchoSphere"
APP_TAGLINE: str = "Professional Message Transmission Interface"
APP_ICON: str = "🛰️"

APP_VERSION: str = "1.0.0"
APP_AUTHOR: str = "Arijit Sen"

# Replace with your actual GitHub repository before submission
APP_GITHUB_URL: str = "https://github.com/your-username/EchoSphere"

# =============================================================================
# Validation Limits
# =============================================================================

MAX_NAME_LENGTH: int = 60
MAX_MESSAGE_LENGTH: int = 2000

MIN_NAME_LENGTH: int = 1
MIN_MESSAGE_LENGTH: int = 1

# =============================================================================
# Tokenizer / Metrics
# =============================================================================

# Approximation used by many LLM providers
CHARS_PER_TOKEN: float = 4.0

# Used for context window visualization
ASSUMED_CONTEXT_WINDOW: int = 8000

# Average reading speed
AVERAGE_READING_WPM: int = 200

# =============================================================================
# Color Palette
# =============================================================================

COLOR_BACKGROUND = "#0E1117"
COLOR_CARD = "#1C1F2B"

COLOR_PRIMARY = "#4F8CFF"
COLOR_SECONDARY = "#7C3AED"

COLOR_SUCCESS = "#10B981"
COLOR_WARNING = "#F59E0B"
COLOR_DANGER = "#EF4444"

COLOR_TEXT = "#FFFFFF"
COLOR_TEXT_MUTED = "#9CA3AF"

# =============================================================================
# Storage
# =============================================================================

HISTORY_FILE_PATH: str = "data/history.json"
CONFIG_FILE_PATH: str = "data/config.json"

MAX_HISTORY_ENTRIES: int = 100

# =============================================================================
# Libraries Used
# =============================================================================

LIBRARIES_USED = [
    "Streamlit",
    "Python",
]

# =============================================================================
# Application Settings
# =============================================================================

DEFAULT_THEME = "dark"

DEFAULT_PAGE_TITLE = APP_NAME

DEFAULT_LAYOUT = "wide"

DEFAULT_SIDEBAR_STATE = "expanded"