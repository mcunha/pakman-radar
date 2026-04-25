import requests


def extract_urls_from_manifest(manifest_data):
    """Extract all valid download URLs from a manifest."""
    urls = []

    def extract_from_dict(d):
        for k, v in d.items():
            if k == "url":
                if isinstance(v, str):
                    urls.append(v)
                elif isinstance(v, list):
                    urls.extend([u for u in v if isinstance(u, str)])
            elif isinstance(v, dict):
                extract_from_dict(v)
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        extract_from_dict(item)

    if isinstance(manifest_data, dict):
        extract_from_dict(manifest_data)

    valid_urls = []
    for u in urls:
        if u.startswith("http") and "$" not in u:
            if "#" in u:
                u = u.split("#")[0]
            valid_urls.append(u)

    return valid_urls


def probe_url(url):
    """Probe a URL to check if it's reachable."""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Scoop-Radar/1.0"}
        # Some servers don't like HEAD requests, we fall back to GET stream
        resp = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
        if resp.status_code in [405, 403, 400]:
            resp = requests.get(url, headers=headers, timeout=5, stream=True)
            resp.close()
        return resp.status_code < 400
    except requests.RequestException:
        return False
