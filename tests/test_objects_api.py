import pytest
import requests

# Test to fetch all the items in the API
def test_list_of_all_objects(api_url_get):
    data = api_url_get
    for object in data:
        # validate that the data in each item is not empty
        assert(object.keys() is not None)
        assert(object['id'] is not None)


# test to validate that API is rendering single item at a time
@pytest.mark.parametrize('id', (3, 5))
def test_single_object_with_id(id):
    params = {'id': id}
    response = requests.get("https://api.restful-api.dev/objects", params=params)
    response.raise_for_status()
    data = response.json()
    # asserting that the rendered item is same as the one given in the request
    assert(int(data[0]['id']) == id)
    assert (data[0].keys() is not None)


# test to validate that the API is returning multiple objects as requested
@pytest.mark.parametrize('id', [('3','5')])
def test_multiple_objects_with_ids(id):
    params = {'id': id}
    response = requests.get("https://api.restful-api.dev/objects", params=params)
    response.raise_for_status()
    data = response.json()

    assert(len(data) == len(id))
    # asserting that the rendered items are same as the one given in the request
    for i in range(len(id)):
        assert(data[i]['id'] == id[i])


# Test to validate that an object can be added to the API
@pytest.mark.parametrize('id', [3,5])
def test_add_object(api_url_get, id):

    # define the JSON for the object to be addded
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

    data = api_url_get

    # Validate the API that the added object is returned
    for object in data:
        if object['id'] == 7:
            assert(object['name'] == 'Apple MacBook Pro 16')
            assert(object['data']['year'] == 2019)
            assert(object['data']['price'] == 1849.99)
            assert(object['data']['CPU model'] == 'Intel Core i9')
            assert(object['data']['Hard disk size'] == '1 TB')
            break


# test to validate that the object can be modified
@pytest.mark.xfail
def test_patch_object(api_url_get):
    data = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }

    # Make a Patch request to an API endpoint
    response = requests.put("https://api.restful-api.dev/objects", json=data, timeout=30)
    response.raise_for_status()

    # Check the status code if is unsuccessful then validate that the item has been updated
    if response.status_code == 200:
        data = api_url_get

        # validating that the modified object is returning the data as given in the request
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















