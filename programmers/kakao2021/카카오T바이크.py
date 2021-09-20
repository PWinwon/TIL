import requests
import json
from bs4 import BeautifulSoup

BASE_URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
X_AUTH_TOKEN = 'a987484307034e8bb9e02adb0d6d8be2'


def get_key(add_url, token, num):
    my_url = BASE_URL + add_url
    head = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json',
    }
    params = {
        'problem': 1,
    }
    response = requests.post(url=my_url, headers=head, params=params).json()
    return response['auth_key']


def get_locations(add_url, key):
    my_url = BASE_URL + add_url
    head = {
        'Authorization': key,
        'Content-Type': 'application/json',
    }
    response = requests.get(my_url, headers=head).json()
    return response['locations']


def get_trucks(add_url, key):
    my_url = BASE_URL + add_url
    head = {
        'Authorization': key,
        'Content-Type': 'application/json',
    }
    response = requests.get(my_url, headers=head).json()
    return response['trucks']


auth_key = get_key('/start', X_AUTH_TOKEN, 1)
# print(auth_key)
locate = get_locations('/locations', auth_key)
N = int(len(locate)**(0.5))
MAP = [[{} for _ in range(N)] for _ in range(N)]
idx = 0
for r in range(N):
    for c in range(N):
        MAP[r][c]['id'] = locate[idx]['id']
        MAP[r][c]['bikes_count'] = locate[idx]['located_bikes_count']
        idx += 1
print(MAP)

trucks = get_trucks('/trucks', auth_key)
print(trucks)