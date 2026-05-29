import pytest

import headers as headers_module

def test_headers_formatter_can_be_instantiated():
    """Verify that the HeadersFormatter can be created without raising an error."""
    # Construct the formatter; the test passes if no exception is raised.
    formatter = headers_module.HeadersFormatter()

