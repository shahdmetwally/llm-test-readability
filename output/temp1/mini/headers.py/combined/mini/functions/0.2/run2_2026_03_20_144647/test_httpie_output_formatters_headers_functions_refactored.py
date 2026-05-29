import pytest

import headers as headers_module

def test_headers_formatter_instantiates_without_error():
    """Ensure HeadersFormatter can be instantiated without raising an exception."""
    # Act: instantiate HeadersFormatter; the test will fail if an exception is raised.
    formatter_instance = headers_module.HeadersFormatter()
    # Assert: we got an instance of the expected class.
    assert isinstance(formatter_instance, headers_module.HeadersFormatter)

