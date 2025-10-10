import pytest
import requests

# There should be an error with status code 400 or 404 for the following tests but this API is not handling any errors
# That is why all these tests have been marked as xfail.

# test to validate that the API throws error for invalid id
@pytest.mark.xfail
@pytest.mark.parametrize('id', ('-3', 'err'))
def test_invalid_id(id):

    params = {'id': id}
    response = requests.get("https://api.restful-api.dev/objects", params=params)
    assert response.status_code == 400 or response.status_code == 404

# test to validate that the API throws error for invalid parameter name
@pytest.mark.xfail
@pytest.mark.parametrize('id', ('3', '5'))
def test_invalid_parameter(id):
    params = {'id23': id}
    response = requests.get("https://api.restful-api.dev/objects", params=params)
    assert response.status_code == 400 or response.status_code == 404


# Test to validate that invalid body for the patch request is not allowed
@pytest.mark.xfail
def test_patch_object_invalid_body(api_url_get):
    data = {
        "description": "Apple MacBook Pro 16 (Updated Name)",
        "age": "error"
    }

    # Make a Patch request to an API endpoint
    response = requests.patch("https://api.restful-api.dev/objects", json=data, timeout=30)

    # Check the status code which should be 400 for bad request as the body has some unwanted fields
    assert response.status_code == 400


# Test to validate that empty body for the patch request is not allowed
@pytest.mark.xfail
def test_patch_object_empty_body(api_url_get):
    data = {
    }

    # Make a Patch request to an API endpoint
    response = requests.patch("https://api.restful-api.dev/objects", json=data, timeout=30)

    # Check the status code which should be 400 for bad request as the body is empty
    assert response.status_code == 400


# Test to validate that the body structure is malformed
@pytest.mark.xfail
def test_patch_object_malformed_body(api_url_get):
    data = {
        ("name"), ("age")
    }

    # Make a Patch request to an API endpoint
    response = requests.patch("https://api.restful-api.dev/objects", json=data, timeout=30)

    # Check the status code which should be 400 for bad request as the body is not a proper json
    assert response.status_code == 400



