import json

import requests

from utils.api_request_data_handler import APIRequestDataHandler


def get_response(url, request_type='GET', headers=None, payload=None):
    """
    Send request to specified url as per request type and returns the response in JSON format.
    :param url - url of the api
    :param request_type - "GET", "POST", "PUT", "DELETE"
    :param headers - To be sent for the specific request
    :param payload - Data to be sent for the request
    """
    response = requests.request(request_type, url, headers=headers, data=payload)
    return response


def get_auth_response(username, password, env: str = "stage"):
    auth_server_url = f'https://{env} url need to be updated'
    request_data = APIRequestDataHandler('authentication')
    payload = request_data.get_modified_payload(username=username, password=password)
    headers = request_data.get_headers()
    print(f"\nGetting token for {username}\n")
    response = get_response(url=auth_server_url, request_type='POST', headers=headers, payload=payload)
    if response.ok:
        print(f'{auth_server_url}  signal sent with payload:\n{payload}')
    else:
        print(f'{auth_server_url} signal sending error: {response}')
    return response


def get_auth_token(username, password, env: str = "stage"):
    auth_response = get_auth_response(username, password, env)
    token = ''
    if auth_response.ok:
        json_response = auth_response.json()
        token = json_response['token']
        print(f'\nToken: {token}\n')
    else:
        print("Token is not found")
    return token


def get_headers_with_auth(username, password, request_data_file, token=None, env: str = "stage"):
    request_data = APIRequestDataHandler(request_data_file)
    if not token:
        token = get_auth_token(username, password, env)
    headers = request_data.get_modified_headers(Authorization=f'Bearer {token}')
    print(f'\n{headers}\n')
    return headers
