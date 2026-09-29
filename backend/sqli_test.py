"""SQL injection test (stub)."""

PAYLOADS = ["' OR '1'='1", "1; DROP TABLE users--"]

def run_sqli_test(endpoint):
    """Send payloads to the endpoint and flag database errors."""
    return []
