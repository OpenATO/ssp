import urllib.request
import os

site = os.environ.get("SITE", "http://civicactions.com")


def test_site_up():
    # FIXME: catch bad URL that fails to resolve
    resp = urllib.request.urlopen(site)

    url = resp.geturl()
    assert "https://" in url, f"no HTTPS in url: {url}"

    code = resp.getcode()
    assert code == 200, f"code: {code}"
