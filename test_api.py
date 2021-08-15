import pytest
import json
import requests

def main_url():
    return 'https://reqres.in'

def test_login_valid():
    url = main_url() + '/api/login/'
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.get(url, data=data)
    token    = json.loads(response.text)
    
    assert response.status_code == 200
    # assert token['token' == "QpwL5tke4Pnpja7X4"
