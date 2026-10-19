import pytest

import httpx


@pytest.mark.parametrize(
    "url,expected",
    [
        ("HTTPS://EXAMPLE.COM:443/a", "https://example.com/a"),
        ("HTTP://EXAMPLE.COM:80/", "http://example.com/"),
        ("WSS://EXAMPLE.COM:443/", "wss://example.com/"),
        ("WS://EXAMPLE.COM:80/", "ws://example.com/"),
        ("FTP://EXAMPLE.COM:21/", "ftp://example.com/"),
        ("HtTpS://EXAMPLE.COM:443/a", "https://example.com/a"),
        ("HTTPS://EXAMPLE.COM:8443/a", "https://example.com:8443/a"),
        ("HTTPS://EXAMPLE.COM/a", "https://example.com/a"),
        ("XYZ://EXAMPLE.COM:443/a", "xyz://example.com:443/a"),
    ],
)
def test_default_port_dropped_for_uppercase_scheme(url: str, expected: str) -> None:
    assert str(httpx.URL(url)) == expected


def test_url_equality_stable_under_reparse() -> None:
    u = httpx.URL("HTTPS://EXAMPLE.COM:443/a")
    assert u == httpx.URL(str(u))
