"""Shared configuration for the Python examples.

Every example is "your existing SDK code, with base_url pointed at the gateway".
This module is the only place that knows the per-protocol path convention, so no
example hardcodes it twice.
"""

import os

BASE_URL = os.environ.get("GATELLM_BASE_URL", "http://localhost:7890").rstrip("/")
API_KEY = os.environ.get("GATELLM_API_KEY", "")
MODEL = os.environ.get("GATELLM_MODEL", "claude-opus-5")

# OpenAI-style clients: the SDK appends /chat/completions, /responses, /embeddings, ...
OPENAI_BASE_URL = f"{BASE_URL}/v1"

# Anthropic-style clients append /v1/messages themselves, so the root is correct.
ANTHROPIC_BASE_URL = BASE_URL

# Google Gen AI appends /v1beta/models/<model>:generateContent itself.
GOOGLE_BASE_URL = BASE_URL


def require_key() -> str:
    if not API_KEY:
        raise SystemExit(
            "GATELLM_API_KEY is not set. Create an access key in the console "
            "(http://localhost:7890) and export it, or copy .env.example to .env."
        )
    return API_KEY
