import pytest

import headers as headers_module

def test_headers_formatter_instantiation():
    """Verify HeadersFormatter can be instantiated without raising an exception."""
    # Constructing the formatter is the behavior under test; storing the instance
    # makes the intent explicit and improves readability.
    formatter = headers_module.HeadersFormatter()
    assert formatter is not None

