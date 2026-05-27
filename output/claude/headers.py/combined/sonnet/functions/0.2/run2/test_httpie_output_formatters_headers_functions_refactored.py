import pytest
import headers as headers

def test_headers_formatter_instantiates_without_error():
    """Test that HeadersFormatter can be instantiated without raising an exception."""
    # Simply constructing the formatter should not raise any exception
    headers.HeadersFormatter()

