EXPECTED_REQUESTS = {
    "http://fake-json-source.com": '{"last_updated": "last tuesday", "values": {"value1": 1, "value2": 2}}',
    "http://fake-csv-source.com": "headline,author,content\nOrcas are surprisingly clever,George Orwhale,Some content about Orcas..."
}


def get(url):
    if url not in EXPECTED_REQUESTS:
        raise ConnectionError(f"fake_requests cannot connect to url: {url}")

    return EXPECTED_REQUESTS[url]
