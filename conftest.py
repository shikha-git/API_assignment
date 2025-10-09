import pytest
import requests

@pytest.fixture()
def api_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()