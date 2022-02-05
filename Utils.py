from logging import exception
import requests
import json
from Exceptions import BadAuthorizationException, TooManyRequestException, NotFoundException, APIException
URL = 'https://challenges.qluv.io/items/'


def callAPI(URL, headers):
    '''A function to make the HTTP request to the server'''
    response_API = requests.get(URL, headers=headers)
    if response_API.ok:
        return response_API.text
    elif response_API.status_code == 401:
        raise BadAuthorizationException
    elif response_API.status_code == 429:
        raise TooManyRequestException
    elif response_API.status_code == 404:
        raise NotFoundException
    else:
        raise APIException
