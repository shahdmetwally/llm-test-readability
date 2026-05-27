import pytest
import headers as headers

def test_headers_formatter_default_instantiation():
    """Verify that HeadersFormatter can be instantiated with default arguments without raising any errors."""
    # Simply constructing the formatter should succeed with no arguments
    headers.HeadersFormatter()

