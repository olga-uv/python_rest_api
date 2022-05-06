import requests
import pytest

#response = requests.get('http://basic-auth/{user}/{passwd}')
#print(response.status_code)
#print(type(response))
#print(response.json())


def test_response_code():
    response = requests.get('https://regres.in/api/users?page=2')

    assert response.status_code == 200


def test_response_code_2():
    response = requests.get('https://reqres.in/api/users?page=2')

    assert response.status_code == 200


user_data = {"name": "morpheus2", "job": "leader2"}


response = requests.post('https://reqres.in/api/users', data=user_data)
print(response.status_code)
print(type(response))
print(response.json())


def test_post_request():
    response3 = requests.post('https://reqres.in/api/users', data=user_data)

    assert response3.status_code == 201

