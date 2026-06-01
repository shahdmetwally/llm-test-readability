import pytest
import headers as headers

def test_headers_formatter_instantiation():
    """Test that HeadersFormatter can be instantiated without errors."""
    # Simply constructing a HeadersFormatter should not raise any exceptions
    headers.HeadersFormatter()

