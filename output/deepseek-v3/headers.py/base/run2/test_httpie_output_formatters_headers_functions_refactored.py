import pytest

import headers as headers_module

def test_headers_formatter_can_be_instantiated():
    """Verify that HeadersFormatter can be instantiated without errors."""
    # This test ensures the class constructor works correctly
    headers_module.HeadersFormatter()

