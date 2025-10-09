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






