from collections import deque


def find_start(n):
    for r in range(n):
        for c in range(n):
            if miro[r][c] == 2:
                return (r, c)
    return False


test_case = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(test_case):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    used = [[0 for _ in range(N)] for _ in range(N)]
    row, col = find_start(N)
    used[row][col] = 1
    que = deque()
    que.append([row, col])
    result = 0
    while que:
        temp = que.popleft()
        row = temp[0]
        col = temp[1]
        if miro[row][col] == 3:
            result = used[row][col]
            break
        for i in range(4):
            rr = row + dr[i]
            cc = col + dc[i]
            if 0 <= rr < N and 0 <= cc < N and used[rr][cc] == 0 and miro[rr][cc] != 1:
                que.append([rr, cc])
                used[rr][cc] += used[temp[0]][temp[1]] + 1
    if result > 0:
        result -= 2

    print('#{} {}'.format(tc+1, result))

#############################################################################################
# 교수님 풀이

# import sys
# sys.stdin = open('text.txt','r')
#
# from collections import deque
#
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
# def bfs(sy,sx):
#     queue = deque()
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#
#     # 시작 지점 큐 등록
#     queue.append((sy,sx,0)) # sy,sx ~ sy,sx 의 최소 이동횟수는 0이다  [0]:y좌표,[1]:x좌표 ,[2] : 최소이동횟수
#     visited[sy][sx] = 1
#
#     # BFS
#     while queue :
#         now = queue.popleft()
#         if MAP[now[0]][now[1]] == 3 : # goal
#             return now[2] - 1
#         for t in range(4): # next 큐등록
#             ny = now[0] + dy[t]
#             nx = now[1] + dx[t]
#             if ny < 0 or nx < 0 or ny >= N or nx >= N : continue
#             if MAP[ny][nx] == 1 : continue # 벽
#             if visited[ny][nx] == 1 : continue
#             visited[ny][nx] = 1 # 재등록 방지
#             queue.append((ny,nx,now[2]+1))
#
#     return 0
#
#
# T = int(input())
#
# for tc in range(1,T+1) :
#     N = int(input())
#     MAP = [
#         list(map(int,input())) for _ in range(N)
#     ]
#
#     # 시작 좌표 찾기
#     flag = 0
#     for y in range(N):
#         for x in range(N):
#             if MAP[y][x] == 2:
#                 sy,sx = y,x
#                 flag = 1
#                 break
#         if flag == 1 : break
#
#     # ret = bfs(sy,sx) (sy,sx) ~  (gy,gx) 의 최소이동횟수
#     ret = bfs(sy,sx)
#     print("#{} {}".format(tc, ret))