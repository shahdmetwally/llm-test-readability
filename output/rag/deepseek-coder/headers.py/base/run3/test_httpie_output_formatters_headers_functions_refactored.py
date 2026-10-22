import pytest
import headers as header

def test_headers_formatter_initialization():
    """
    Test that the HeadersFormatter class can be initialized without error.
    """
    # Setup
    formatter = header.HeadersFormatter()

    # Verify
    # Here we're using pytest's assert functionality to verify that the HeadersFormatter class was initialized without error.
    assert isinstance(formatter, header.HeadersFormatter)

