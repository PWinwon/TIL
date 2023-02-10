import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input().strip())

for tc in range(T):
    R, C = map(int, input().split())
    MAP = [list(input().strip()) for _ in range(R)]
    used = [[0 for _ in range(C)] for _ in range(R)]

    key_dict = dict()

    for i in range(26):
        key_dict[chr(ord('A')+i)] = 0

    key_str = input().strip()
    if key_str != '0':
        for k in key_str:
            key_dict[k.upper()] += 1

    que = deque()
    cnt = 0
    result = 0

    for r in range(R):
        for c in range(C):
            if (r == 0 or r == R-1 or c == 0 or c == C-1):
                if MAP[r][c] == '.':
                    que.append([r, c])
                    used[r][c] = 1
                    cnt += 1
                elif MAP[r][c] == '$':
                    result += 1
                    MAP[r][c] = '.'
                    que.append([r, c])
                    used[r][c] = 1
                elif ord('A') <= ord(MAP[r][c]) <= ord('Z'):
                    if key_dict[MAP[r][c]]:
                        que.append([r, c])
                        MAP[r][c] = '.'
                        used[r][c] = 1
                        cnt += 1
                    else:
                        que.append([r, c])
                        used[r][c] = 1
                elif ord('a') <= ord(MAP[r][c]) <= ord('b'):
                    key_dict[MAP[r][c].upper()] += 1
                    que.append([r, c])
                    MAP[r][c] = '.'
                    used[r][c] = 1
                    cnt += 1

    de = -1
    while True:
        next_que = deque()
        next_cnt = 0
        now_cnt = 0
        while que:
            y, x = que.popleft()
            now_cnt += 1
            # 통과하지 못하는 문이 들어온 경우
            if ord('A') <= ord(MAP[y][x]) <= ord('Z') and key_dict[MAP[y][x]] == 0:
                next_que.append([y, x])
                next_cnt += 1
                continue
            for i in range(4):
                yr, xr = y+dr[i], x+dc[i]
                if yr < 0 or yr >= R or xr < 0 or xr >= C:
                    continue
                # 이미 방문한 곳인 경우
                elif used[yr][xr]:
                    continue
                # 벽일 경우
                elif MAP[yr][xr] == '*':
                    continue
                # 빈공간일경우
                elif MAP[yr][xr] == '.':
                    que.append([yr, xr])
                    used[yr][xr] = 1
                    continue
                # 문일경우
                elif ord('A') <= ord(MAP[yr][xr]) <= ord('Z'):
                    # 통과 가능한경우
                    if key_dict[MAP[yr][xr]]:
                        MAP[yr][xr] = '.'
                        que.append([yr, xr])
                        used[yr][xr] = 1
                        continue
                    # 통과 불가능한경우
                    else:
                        next_que.append([yr, xr])
                        used[yr][xr] = 1
                        next_cnt += 1
                # 열쇠일경우
                elif ord('a') <= ord(MAP[yr][xr]) <= ord('z'):
                    key_dict[MAP[yr][xr].upper()] += 1
                    MAP[yr][xr] = '.'
                    used[yr][xr] = 1
                    que.append([yr, xr])
                # 문서일 경우
                elif MAP[yr][xr] == '$':
                    result += 1
                    MAP[yr][xr] = '.'
                    que.append([yr, xr])
                    used[yr][xr] = 1

        if now_cnt == cnt:
            break
        cnt = next_cnt
        que = next_que
    print(result)