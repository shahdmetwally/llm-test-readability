import pytest
import headers as headers

def test_headers_formatter_instantiation_succeeds():
    """Test that HeadersFormatter can be instantiated without raising any exceptions."""
    # Instantiate HeadersFormatter; the test passes if no exception is raised
    headers.HeadersFormatter()

