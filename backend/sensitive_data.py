"""Sensitive data exposure check (stub)."""

SENSITIVE_KEYS = ["password", "token", "secret", "api_key"]

def check_sensitive_data(response_json):
    """Return keys that leak sensitive data."""
    return [k for k in response_json if k.lower() in SENSITIVE_KEYS]
