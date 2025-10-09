import pytest
import requests

def api_url():
    response = requests.get("https://api.restful-api.dev/objects")
    response.raise_for_status()
    return response.json()