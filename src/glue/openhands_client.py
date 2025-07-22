import os
import requests

OPENHANDS_API = os.getenv("OPENHANDS_API", "http://openhands:3000/api")

def forward_to_openhands(payload: dict):
    """Send payload to OpenHands server."""
    resp = requests.post(OPENHANDS_API, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()
