import sys
from heapq import heappop, heappush


def move_player():
    global N, M
    for m in range(M):
        de = -1
        r, c, d, s, g = player[m]
        # 기존 location에서 빼주기
        location[r][c] = -1
        # 격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서 1만큼 이동
        if r+dr[d] < 0 or r+dr[d] >= N or c+dc[d] < 0 or c+dc[d] >= N:
            d = (d + 2) % 4
            # 방향 바뀌면 적용
            player[m][2] = d
        # 플레이어 한칸 이동
        r += dr[d]
        c += dc[d]

        # 이동한 위치를 player 배열 및 location에 반영
        player[m][0], player[m][1] = r, c

        # 이동 후 플레이어가 존재한다면 결투 진행
        de = -1
        if location[r][c] >= 0:
            fight(m, location[r][c])
            continue
        elif GUNS[r][c]:
            get_gun(m)
            # 총을 획득했다는 건, 결투할 일 없으니 location에 반영
        location[r][c] = m


def get_gun(m):
    r, c, d, s, g = player[m]
    if g:
        heappush(GUNS[r][c], [-g, g])
    player[m][4] = heappop(GUNS[r][c])[1]
    return


# 플레이어 idx a, b를 입력받는다
def fight(a, b):
    # 둘의 능력치를 비교한다
    ar, ac, ad, astat, agun = player[a]
    br, bc, bd, bstat, bgun = player[b]

    # 능력치 + 총의 공격력 합이 큰쪽이 승리
    # 같다면 초기 능력치가 높은 쪽이 승리
    # 진 플레이어는 칸에 총을 내려두고 추방
    # 이긴 플레이어는 칸에서 총 쇼핑
    gap = (astat+agun) - (bstat+bgun)
    # a 승
    if gap > 0:
        # 승자는 점수를 획득
        SCORE[a] += gap
        # 패자는 총을 버리고 쫓겨난다
        drop_gun(b)
        get_out(b)
        # 승자 location 반영
        location[ar][ac] = a
        # 승자 총 획득
        # 자리에 총 있는지 먼저 확인
        if GUNS[ar][ac]:
            get_gun(a)
    # b 승
    elif gap < 0:
        SCORE[b] -= gap
        drop_gun(a)
        get_out(a)
        location[br][bc] = b
        if GUNS[br][bc]:
            get_gun(b)
    # 무승부
    # gap 어차피 0이니까 증가 필요 x
    else:
        # a 승 (초기 능력 승)
        if astat > bstat:
            drop_gun(b)
            get_out(b)
            location[ar][ac] = a
            if GUNS[ar][ac]:
                get_gun(a)
        # b 승 (초기 능력 승)
        else:
            drop_gun(a)
            get_out(a)
            location[br][bc] = b
            if GUNS[br][bc]:
                get_gun(b)


def drop_gun(m):
    r, c, d, s, g = player[m]
    if g:
        heappush(GUNS[r][c], [-g, g])
        player[m][4] = 0
    return


def get_out(m):
    global N
    r, c, d, s, g = player[m]
    while True:
        yr, xr = r+dr[d], c+dc[d]
        if yr < 0 or yr >= N or xr < 0 or xr >= N:
            d = (d + 1) % 4
            continue
        elif location[yr][xr] >= 0:
            d = (d + 1) % 4
            continue
        player[m][0] = yr
        player[m][1] = xr

        # 방향도 최신화
        player[m][2] = d

        # 총이 있다면 획득
        if GUNS[yr][xr]:
            get_gun(m)

        # 추방당한 위치 반영
        location[yr][xr] = m
        break


# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

#    상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M, K = map(int, input().split())

GUNS = [[[] for _ in range(N)] for _ in range(N)]
temp = [list(map(int, input().split())) for _ in range(N)]
for r in range(N):
    for c in range(N):
        if temp[r][c] != 0:
            heappush(GUNS[r][c], [-temp[r][c], temp[r][c]])

# r, c, d: 방향, s: 능력치, 0: gun power
player = []
location = [[-1 for _ in range(N)] for _ in range(N)]
for m in range(M):
    r, c, d, s = map(int, input().split())
    player.append([r-1, c-1, d, s, 0])
    location[r-1][c-1] = m

SCORE = [0 for _ in range(M)]

for k in range(K):
    move_player()
print(' '.join(map(str, SCORE)))