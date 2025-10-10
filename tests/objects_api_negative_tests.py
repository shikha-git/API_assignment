import pytest
import requests

@pytest.mark.parametrize('id', ('-3', 'err'))
def test_invalid_id(id):

    params = {'id': id}
    response = requests.get("https://api.restful-api.dev/objects", params=params)
    response.raise_for_status()
    data = response.json()
    assert len(data) == 0

# There should be the error with status code 400 that it is an invalid parameter value


@pytest.mark.parametrize('id', ('3', '5'))
def test_invalid_parameter(id):
    params = {'id23': id}
    response = requests.get("https://api.restful-api.dev/objects", params=params)
    response.raise_for_status()
    data = response.json()
    assert len(data) == 1

# Here the API should throw proper error message with 400 status code that the parameter give is invalid.
# its accepting any random value fpr any parameter.

# Test to validate that invalid body for the patch request is not allowed
def test_patch_object_invalid_body(api_url_get):
    data = {
        "description": "Apple MacBook Pro 16 (Updated Name)",
        "age": "error"
    }

    # Make a Patch request to an API endpoint
    response = requests.put("https://api.restful-api.dev/objects", json=data, timeout=30)
    response.raise_for_status()

    # Check the status code which should be 400 for bad request as the body has some unwanted fields
    assert response.status_code == 400



# Test to validate that empty body for the patch request is not allowed
def test_patch_object_empty_body(api_url_get):
    data = {
    }

    # Make a Patch request to an API endpoint
    response = requests.put("https://api.restful-api.dev/objects", json=data, timeout=30)
    response.raise_for_status()

    # Check the status code which should be 400 for bad request as the body is empty
    assert response.status_code == 400


# Test to validate that the body structure is malformed
def test_patch_object_malformed_body(api_url_get):
    data = {
        ("name"), ("age")
    }

    # Make a Patch request to an API endpoint
    response = requests.put("https://api.restful-api.dev/objects", json=data, timeout=30)
    response.raise_for_status()

    # Check the status code which should be 400 for bad request as the body is not a proper json
    assert response.status_code == 400



