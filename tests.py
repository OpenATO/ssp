# tests.py
import requests

def check_protocol(domain: str) -> str:
    """Checks if the domain uses HTTP or HTTPS."""
    try:
        response = requests.head(f"http://{domain}", allow_redirects=True, timeout=5)
        protocol = response.url.split(":")[0]
        return protocol
    except requests.RequestException as e:
        print(f"Error: {e}")
        return "error"

def check_reachability(domain: str) -> bool:
    """Checks if the domain is reachable."""
    try:
        response = requests.head(f"http://{domain}", allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error: {e}")
        return False
