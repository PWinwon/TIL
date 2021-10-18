import requests
import json
from bs4 import BeautifulSoup

# 그냥 돌리면 fail 351 score 229.94747899159663 
# 내가 사용한 알고리즘 fail 168 score 261.55142156862746 distance 1180.6

BASE_URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
X_AUTH_TOKEN = 'c3b209277de88f177d0a3834a58a587b'


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
            {'truck_id': 0, 'command': coms[0]},
            {'truck_id': 1, 'command': coms[1]},
            {'truck_id': 2, 'command': coms[2]},
            {'truck_id': 3, 'command': coms[3]},
            {'truck_id': 4, 'command': coms[4]},
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


def truck_move(t_loc, i_loc):
    while t_loc != i_loc:
        if (t_loc % 5) < (i_loc % 5):
            ps_params[i].append(1)
            t_loc += 1
        elif (t_loc % 5) > (i_loc % 5):
            ps_params[i].append(3)
            t_loc -= 1
        if (t_loc // 5) < (i_loc // 5):
            ps_params[i].append(2)
            t_loc += 5
        elif (t_loc // 5) > (i_loc // 5):
            ps_params[i].append(4)
            t_loc -= 5
    return


auth_key = get_key('/start', X_AUTH_TOKEN, 1)
locate = get_locations('/locations', auth_key)
N = int(len(locate)**(0.5))
# MAP = [[0 for _ in range(N)] for _ in range(N)]
# auth_key = '12f7def9-2d11-4827-8d33-2a9a11d63ac7'
# print(auth_key)
for ii in range(720):
    locate = get_locations('/locations', auth_key)
    trucks = get_trucks('/trucks', auth_key)
    trucks_loc = []
    for i in range(N):
        trucks_loc.append(trucks[i]['location_id'])
    ps_params = [[], [], [], [], []]
    idx = 0
    for idx in range(N*N):
        i = idx // 5
        lbc = locate[idx]['located_bikes_count']
        # MAP[N-1-idx%N][i] = lbc
        if len(ps_params[i]) > 10:
            continue
        if lbc > 2:
            truck_loc = trucks_loc[i]
            truck_move(truck_loc, idx)
            ps_params[i].append(5)
            trucks_loc[i] = idx
        elif lbc < 2:
            truck_loc = trucks_loc[i]
            truck_move(truck_loc, idx)
            ps_params[i].append(6)
            trucks_loc[i] = idx
    ps = put_simulate('/simulate', auth_key, ps_params)
    # print(ps)

# score = get_score('/score', auth_key)
# print(score)

