import pytest
import headers as headers_module

def test_headers_formatter_instantiation():
    """Test that HeadersFormatter can be instantiated without errors."""
    formatter = headers_module.HeadersFormatter()

