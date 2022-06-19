import requests
import pytest

base_url = 'https://api-ssl.bitly.com/v4/'
token = 'f53e63a197998dc12679944b467c81df719bdd28'


@pytest.fixture()
def user_email():
    email = 'leonteva.h@gmail.com'
    return email


def test_get_user_profile(user_email):
    headers = {"Authorization": f'Bearer {token}'}
    response = requests.get(f'{base_url}user', headers=headers)
    print(response.text)
    print(response.status_code)

    assert response.json()['emails'][0]['email'] == user_email

