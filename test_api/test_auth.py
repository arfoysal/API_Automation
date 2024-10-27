from os.path import join


from test_api.base_test import BaseTest
from utils.app_constants import AppConstant
from utils.request_handler import *

from jsonschema.validators import validate


class TestAuth(BaseTest):

    def test_valid_auth_response(self):
        response = get_auth_response(username="abd@update.com", password="Admin1233$1245")
        assert response.status_code == 200
        assert response.reason == 'OK'
        print(response.json())
        print(response.headers)
        json_response = response.json()
        assert json_response['token']
        with open(join(AppConstant.RESPONSE_SCHEMA, 'auth_valid.json'), 'r') as json_file:
            expected_schema = json.loads(json_file.read())
        assert validate(json_response, expected_schema) is None

    def test_auth_with_invalid_password(self):
        response = get_auth_response(username="abd@update.com", password="Admin123$12")
        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        json_response = response.json()
        assert json_response['timestamp']
        assert json_response['status'] == 401
        assert json_response['error'] == 'Unauthorized'
        assert json_response['message'] == 'Provider account is not active.'
        assert json_response['path'] == '/token'
        with open(join(AppConstant.RESPONSE_SCHEMA, 'auth_invalid.json'), 'r') as json_file:
            expected_schema = json.loads(json_file.read())
        assert validate(json_response, expected_schema) is None

    def test_collect_header(self):
        get_headers_with_auth(username="abd@update.com", password="Admin123$1245",
                              request_data_file='authentication')

    def test_api_response(self):
        url = 'URL'
        response = get_response(url=url, request_type='HEAD')
        assert response.status_code == 204
        assert response.reason == 'No Content'