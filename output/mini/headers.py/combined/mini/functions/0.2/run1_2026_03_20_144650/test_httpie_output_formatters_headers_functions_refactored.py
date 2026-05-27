import pytest

import headers as headers_module

def test_headers_formatter_constructs_without_exception():
    """Ensure HeadersFormatter can be instantiated without raising an exception."""
    # Instantiate the formatter; the test succeeds if no exception is raised.
    formatter = headers_module.HeadersFormatter()

