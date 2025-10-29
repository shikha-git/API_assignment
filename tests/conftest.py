import pytest
import requests

url = "https://api.restful-api.dev/objects"

# this fixture can be used to call GET request for an url
@pytest.fixture(scope='function')
def api_url_get(params=None, headers=None, json=None): # sending optional parameters
    if json is not None and headers is not None and params is not None:
        response = requests.get(url, params=params, headers=headers, json=json)
    elif params is not None and headers is not None:
        response = requests.get(url, params=params, headers=headers)
    elif params is not None:
        response = requests.get(url, params=params)
    else:
        response = requests.get(url)

    # returning status error if any
    response.raise_for_status()

    # the fixture would return the response in JSON format
    return response.json()


# this fixture can be used to call POST request for an url
@pytest.fixture(scope='function')
def api_url_post(params=None, headers=None, json=None):
    if json is not None and headers is not None and params is not None:
        response = requests.post(url, params=params, headers=headers, json=json)
    elif params is not None and headers is not None:
        response = requests.post(url, params=params, headers=headers)
    elif params is not None:
        response = requests.post(url, params=params)
    else:
        response = requests.post(url)

    # returning status error if any
    response.raise_for_status()

    # the fixture would return the response in JSON format
    return response.json()
