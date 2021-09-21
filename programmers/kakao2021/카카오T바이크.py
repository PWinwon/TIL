import requests
import json
from bs4 import BeautifulSoup

BASE_URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
X_AUTH_TOKEN = 'd619fa72296c3c7051139053b664800b'


def get_key(add_url, token, num):
    my_url = BASE_URL + add_url
    head = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json',
    }
    params = {
        'problem': num,
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


def put_simulate(add_url, key, coms):
    my_url = BASE_URL + add_url
    head = {
        'Authorization': key,
        'Content-Type': 'application/json',
    }
    data = {
        'commands':[
            {'truck_id': 0, 'command': [0]},
            {'truck_id': 1, 'command': [0]},
            {'truck_id': 2, 'command': [0]},
            {'truck_id': 3, 'command': [0]},
            {'truck_id': 4, 'command': [0]},
        ]
    }
    response = requests.put(my_url, headers=head, data=json.dumps(data)).json()
    return response


def get_score(add_url, key):
    my_url = BASE_URL + add_url
    head = {
        'Authorization': key,
        'Content-Type': 'application/json',
    }
    response = requests.get(my_url, headers=head).json()
    return response


auth_key = get_key('/start', X_AUTH_TOKEN, 1)
locate = get_locations('/locations', auth_key)
N = int(len(locate)**(0.5))
MAP = [[0 for _ in range(N)] for _ in range(N)]
# auth_key = '12f7def9-2d11-4827-8d33-2a9a11d63ac7'
# print(auth_key)
for ii in range(720):
    locate = get_locations('/locations', auth_key)
    trucks = get_trucks('/trucks', auth_key)
    ps_params = [[], [], [], [], []]
    idx = 0
    for idx in range(N*N):
        i = idx // 5
        lbc = locate[idx]['located_bikes_count']
        MAP[N-1-idx%N][i] = lbc

    ps = put_simulate('/simulate', auth_key, ps_params)
    print(ps)

score = get_score('/score', auth_key)
print(score)

