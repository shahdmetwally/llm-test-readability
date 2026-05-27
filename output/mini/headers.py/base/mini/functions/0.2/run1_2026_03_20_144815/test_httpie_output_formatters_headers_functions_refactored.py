import pytest

import headers as headers_module

def test_headers_formatter_instantiation():
    """Instantiating HeadersFormatter should succeed without raising an exception."""
    # Construct the HeadersFormatter from the headers module (alias: headers_module).
    formatter = headers_module.HeadersFormatter()
    # Successful construction (no exception) is the intent of this test.

