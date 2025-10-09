import pytest
import requests

@pytest.mark.smoke
def test_list_of_all_objects():

    response = requests.get("https://api.restful-api.dev/objects")
    response.raise_for_status()
    data = response.json()

    for object in data:
        print(object)
        print(object['id'])
        assert(object.keys() is not None)
        assert(object['id'] is not None)


@pytest.mark.parametrize('id', (3, 5))
def test_single_object_with_id(id):
    params = {'id': id}
    response = requests.get("https://api.restful-api.dev/objects", params=params)
    response.raise_for_status()

    data = response.json()

    assert(int(data[0]['id']) == id)


@pytest.mark.parametrize('id', [('3','5')])
def test_multiple_objects_with_ids(id):
    params = {'id': id}
    response = requests.get("https://api.restful-api.dev/objects", params=params)
    response.raise_for_status()

    data = response.json()

    assert(len(data) == len(id))
    for i in range(len(id)):
        assert(data[i]['id'] == id[i])


def test_add_object():
    data = {
       "name": "Apple MacBook Pro 16",
       "data": {
          "year": 2019,
          "price": 1849.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
       }
    }
    headers = {"content-type": "application/json"}

    response = requests.post("https://api.restful-api.dev/objects", headers=headers ,json=data, timeout=30)
    response.raise_for_status()

    response = requests.get("https://api.restful-api.dev/objects")
    response.raise_for_status()

    data = response.json()
    for object in data:
        if object['id'] == 7:
            assert(object['name'] == 'Apple MacBook Pro 16')
            assert(object['data']['year'] == 2019)
            assert(object['data']['price'] == 1849.99)
            assert(object['data']['CPU model'] == 'Intel Core i9')
            assert(object['data']['Hard disk size'] == '1 TB')
            break


def test_update_object():
    data = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }

    # Make a Patch request to an API endpoint
    response = requests.put("https://api.restful-api.dev/objects", json=data, timeout=30)
    response.raise_for_status()

    # Check the status code
    if response.status_code == 200:
        response = requests.get("https://api.restful-api.dev/objects")
        response.raise_for_status()

        data = response.json()
        print(data)
        for object in data:
            if object['id'] == 7:
                assert (object['name'] == 'Apple MacBook Pro 16 (Updated Name)')
                break

    elif response.status_code == 404:
        print("API request failed: Resource not found (status code 404).")
    elif response.status_code == 500:
        print("API request failed: Internal server error (status code 500).")
    else:
        print(f"API request returned an unexpected status code: {response.status_code}")

        # Alternatively, use raise_for_status() to automatically raise an exception for bad status codes
        response.raise_for_status()
        print("API request was successful according to raise_for_status().")















