import requests
import pytest

from assertions import Assertions
base_url = "https://reqres.in"
request_url = "/api/login"
token = ""

# def setup():
#     login_data = {
#         "email": "eve.holt@reqres.in",
#         "password": "citylicka"
#     }
#
#     response1 = requests.post(base_url + request_url, data=login_data)
#     token = response1.json()['token']
#     print(token)


def test_1():
    data = {"name": "morpheus",
            "job": "zion resident"
            }
    headers = {'token': token}

    response2 = requests.put(base_url + '/api/users/2', data=data, headers=headers)
    assert response2.status_code == 200
    Assertions.assert_json_value_by_name(response2, "name", "morpheus")
    Assertions.assert_json_value_by_name(response2, "job", "zion resident")
    print(response2.request.body)
    print(response2.text)
