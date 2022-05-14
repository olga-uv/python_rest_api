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
    if key in parsed_response['slideshow']['slides'][1]:
        if len(parsed_response['slideshow']['slides'][1][key]) != 0:
            assert len(parsed_response['slideshow']['slides'][1][key]) != 0
        else:
            print(f'Field {key} is empty')
            assert False
    else:
        print(f'Field {key} is not in {httpbin_url}' + '/json')
        assert False


def test_get_redirect_history():
    count = '2'
    response = requests.get(httpbin_url + 'redirect/' + count)
    #print(response.text)
    assert int(count) == len(response.history)


def test_get_user_data():
    user_id = '1'
    response = requests.get(regres_url + 'api/users/' + user_id)
    assert 'id' in response.json()['data'], '"id" is not in object '
    assert 'email' in response.json()['data'], '"email" is not in object '
    assert 'first_name' in response.json()['data'], '"first_name" is not in object '
    assert 'last_name' in response.json()['data'], '"last_name" is not in object '
    assert 'avatar' in response.json()['data'], '"avatar" is not in object '


def test_not_long_string():
    not_long_string = input().replace(" ", "")
    assert len(not_long_string) <= 30, f'{not_long_string} contains more than 30 symbols'


def test_status_code_verification():
    for codes in ['200', '300', '400', '500']:
        response = requests.get(httpbin_url + 'status/' + codes)
        assert int(codes) == response.status_code
