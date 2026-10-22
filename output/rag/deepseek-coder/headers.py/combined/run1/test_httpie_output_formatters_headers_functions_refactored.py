import headers as http

def test_headers_formatter_initialisation():
    formatter = HeadersFormatter()
    assert formatter.headers == []
    assert formatter.request_type == None