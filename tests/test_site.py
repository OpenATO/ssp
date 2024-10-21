import urllib.request

url = "http://performance.gov"


def test_site_up():
    # FIXME: catch bad URL that fails to resolve
    resp = urllib.request.urlopen(url)

    site = resp.geturl()
    assert "https://" in site, f"site: {site}"

    code = resp.getcode()
    assert code == 200, f"code: {code}"
