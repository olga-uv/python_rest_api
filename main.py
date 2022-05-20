import requests
import pytest
import datetime


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


#response = requests.post('https://reqres.in/api/users', data=user_data)
#print(response.status_code)
#print(type(response))
#print(response.json())


def test_post_request():
    response3 = requests.post('https://reqres.in/api/users', data=user_data)

    assert response3.status_code == 201


def test_get_users():
    response = requests.get('https://reqres.in/api/users?page=2')
    parsed_response = response.json()
    '''
    Выбираем email для 3го пользователя из списка
    '''
    print(parsed_response)
    print(parsed_response['data'][2]['email'])
    assert parsed_response['data'][2]['email'] == "tobias.funke@reqres.in"
    assert len(parsed_response['data']) == 6


httpbin_url = 'http://httpbin.org/'
regres_url = 'https://reqres.in/'


def test_get_items():
    response = requests.get(httpbin_url + 'json')
    parsed_response = response.json()
    key = 'items'
    response_items = parsed_response['slideshow']['slides'][1]

    assert key in response_items, f'Field {key} is not in {httpbin_url} json'
    assert len(response_items[key]) != 0, f'Field {key} is empty'


def test_get_redirect_history():
    count = '2'
    response = requests.get(f'{httpbin_url}redirect/{count}')

    assert len(response.history) == int(count)


def test_get_user_data():
    user_id = '1'
    response = requests.get(f'{regres_url}api/users/{user_id}')

    assert 'id' in response.json()['data'], '"id" is not in object '
    assert 'email' in response.json()['data'], '"email" is not in object '
    assert 'first_name' in response.json()['data'], '"first_name" is not in object '
    assert 'last_name' in response.json()['data'], '"last_name" is not in object '
    assert 'avatar' in response.json()['data'], '"avatar" is not in object '


def test_not_long_string():
    not_long_string = input().replace(" ", "")
    assert len(not_long_string) <= 2, f'{not_long_string} contains more than 30 symbols'


@pytest.mark.parametrize('code', ['200', '300', '400', '500'])
def test_status_code_verification(code):
    response = requests.get(f'{httpbin_url}status/{code}')

    assert response.status_code == int(code)


now = int(datetime.datetime.now().strftime('%Y%m%d'))
print(now)


@pytest.mark.skipif("now < 20220520")
@pytest.mark.parametrize("email, password", [('eve.holt@reqres.in', 'pistol'), ('eve.holt@reqres.in', 'pistol')])
def test_registration(email, password):
    register_user_data = {"email": email, "password": password}
    response = requests.post(f'{regres_url}api/register', register_user_data)

    assert response.status_code == 200

