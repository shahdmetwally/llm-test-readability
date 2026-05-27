import headers as headers

def test_headers_formatter_instantiation():
    # Given
    expected_headers = headers.HeadersFormatter()

    # When
    actual_headers = module_0.HeadersFormatter()

    # Then
    assert actual_headers == expected_headers

