import pytest

import headers as headers_module

def test_headers_formatter_initializes_without_error():
    """Ensure HeadersFormatter can be instantiated without raising an exception."""
    # Instantiate the HeadersFormatter to verify construction succeeds.
    headers_formatter = headers_module.HeadersFormatter()
    # The test passes if construction completes without raising.
    assert headers_formatter is not None

