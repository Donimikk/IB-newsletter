# ===========================================
# IB Newsletter - Config Package
# ===========================================
# Tento súbor označuje priečinok config/ ako Python package
# ===========================================

from .settings import (
    OPENAI_API_KEY,
    BREVO_API_KEY,
    BREVO_SENDER_EMAIL,
    BREVO_SENDER_NAME,
    BREVO_LIST_ID,
    MODE,
    TEST_EMAIL,
    NEWSLETTER_CONFIG,
    API_SOURCES,
    GPT_CONFIG,
    validate_config,
)

__all__ = [
    "OPENAI_API_KEY",
    "BREVO_API_KEY",
    "BREVO_SENDER_EMAIL",
    "BREVO_SENDER_NAME",
    "BREVO_LIST_ID",
    "MODE",
    "TEST_EMAIL",
    "NEWSLETTER_CONFIG",
    "API_SOURCES",
    "GPT_CONFIG",
    "validate_config",
]
