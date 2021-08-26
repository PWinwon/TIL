#############################################################
# bfs  구현 1번부터 출발하여 노드번호, level 출력

# from collections import deque

# adj = [[0 for _ in range(8)] for _ in range(8)]
#
# adj[1][2] = 1
# adj[1][3] = 1
# adj[2][5] = 1
# adj[3][7] = 1
# adj[4][2] = 1
# adj[4][6] = 1
# adj[5][6] = 1
# adj[6][4] = 1
# adj[7][3] = 1
# adj[7][6] = 1
#
# que = deque()
# que.append(1)
# used = [0] * 8
# used[1] = 1
# result = []
# while que:
#     temp = que.popleft()
#     result.append(temp)
#     for i in range(1, 8):
#         if used[i] == 0 and adj[temp][i] == 1:
#             que.append(i)
#             used[i] = used[temp] + 1
#
#
# print('탐색 순서 : {}'.format(' '.join(map(str, result))))
# for j in range(1, 8):
#     print('{}번 노드 : {}'.format(j, used[j]))

#############################################################
# bfs  구현 1번부터 출발하여 노드번호, level 출력 - 교수님 풀이

# adj = [
#     [0 for _ in range(8)] for _ in range(8)
# ]
#
# adj[1][2] = 1
# adj[1][3] = 1
# adj[2][5] = 1
# adj[3][7] = 1
# adj[4][2] = 1
# adj[4][6] = 1
# adj[5][6] = 1
# adj[6][4] = 1
# adj[7][3] = 1
# adj[7][6] = 1
#
# from collections import deque
#
# def bfs(start):
#     queue = deque()
#     visited = [0 for _ in range(8)] # 1또는0 큐에 재등록 방지
#     level  = [0 for _ in range(8)] # level 몇에 탐색 되었는지 저장
#
#     queue.append(start)
#     level[start] = 0 # level 0부터 시작
#     visited[start] = 1 # 큐에 재등록 방지
#
#     while queue : # 방문 예약 있을때
#         now  = queue.popleft()
#         # 탐색
#         print("{} level : {}".format(now, level[now]))
#         for next in range(1,8): # 연결되있는 노드 큐에 등록 (방문 예약 )
#             if adj[now][next] == 0 : continue
#             if visited[next] == 1 : continue
#             visited[next] = 1 # 큐에 재등록 방지
#             level[next] = level[now] + 1
#             queue.append(next)
#
# bfs(1)

#############################################################
# 대각선 4군데 중 가장 큰 값 찾기

# def find_max(r, c):
#     max_val = 0
#     for i in range(4):
#         if max_val < lst[r+dr[i]][c+dc[i]]:
#             max_val = lst[r+dr[i]][c+dc[i]]
#     return max_val
#
# #     우상 우하 좌상 좌하
# dr = [-1, 1, -1, 1]
# dc = [1, 1, -1, -1]
#
# lst = [
#     [3, 2, 1, 7],
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [1, 1, 1, 1],
# ]
#
# a = find_max(2, 2)
# print(a)

#############################################################
# 대각선 4군데 중 가장 큰 값 찾기 - 교수님 풀이

# MAP = [
#     [3,2,1,7],
#     [1,2,3,4],
#     [5,6,7,8],
#     [1,1,1,1]
# ]
#
# dr = [-1,-1,1,1]
# dc = [-1,1,-1,1]
#
# r,c = map(int,input().split())
#
# max_val = int(-21e8)
# max_point = (-1,-1)
# for t in range(4) :
#     nr = r + dr[t]
#     nc = c + dc[t]
#     if nr < 0 or nc < 0 or nr >= 4 or nc >= 4 : continue
#     # max_val vs MAP[nr][nc]
#     if max_val < MAP[nr][nc] :
#         max_val = MAP[nr][nc]
#         max_point = (nr,nc)
#
# print("{} : {}".format(max_val , max_point))

#############################################################
# 화단에 꽃 피우기

# from collections import deque
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# ans = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]
# ans[0][0] = 1
# que = deque()
# que.append([0, 0])
# while que:
#     temp = que.popleft()
#     row = temp[0]
#     col = temp[1]
#     for i in range(4):
#         r = row + dr[i]
#         c = col + dc[i]
#         if r < 0 or r > 2 or c < 0 or c > 4:
#             continue
#         if ans[r][c] > 0:
#             continue
#         ans[r][c] = ans[row][col] + 1
#         que.append([r, c])
#
# for j in range(3):
#     print(' '.join(map(str, ans[j])))

#############################################################
# 화단에 꽃 피우기 - 교수님 풀이

# MAP = [
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
# ]
#
# from collections import deque
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
# def bfs(sy,sx):
#     visited = [[0 for _ in range(5)] for _ in range(3)]
#     queue = deque()
#     queue.append((sy,sx))
#     visited[sy][sx] = 1
#     MAP[sy][sx] = 1
#     ans = -int(21e8)
#     # BFS 시작
#     while queue :
#         y,x = queue.popleft()
#         ans = MAP[y][x] # ans vs MAP[y][x]
#         for t in range(4) : # 다음 정점 큐등록 (상하좌우)
#             ny = y + dy[t]
#             nx = x + dx[t]
#             if ny < 0 or nx < 0 or ny >= 3 or nx >= 5 : continue
#             if visited[ny][nx] == 1 : continue
#             MAP[ny][nx] = MAP[y][x] + 1 # 다음 노드의 날짜를 기록
#             visited[ny][nx] = 1
#             queue.append((ny,nx))
#
#     return ans
#
# ret = bfs(0,0)
# print(ret)

#############################################################
# 화단에 꽃 피우기 - 교수님 풀이-2

# from collections import deque
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
# def bfs(sy,sx):
#     visited = [[0 for _ in range(5)] for _ in range(3)]
#     queue = deque()
#     queue.append((sy,sx,1))
#     visited[sy][sx] = 1
#     ans = 0
#     while queue :
#         now = queue.popleft() # [0]:y  [1]:x  // [2]: level
#         ans = now[2]
#         for t in range(4):
#             ny = now[0] + dy[t]
#             nx = now[1] + dx[t]
#             if ny < 0 or nx < 0 or ny >= 3 or nx >= 5: continue
#             if visited[ny][nx] == 1 : continue
#             visited[ny][nx] = 1
#             queue.append((ny,nx,now[2]+1))
#
#     return ans
#
# ret = bfs(0,0)
# print(ret)


#############################################################
# 화단에 꽃 피우기 좌표 2개

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

ans[1][1] = 1
ans[0][4] = 1
que = deque()
que.append([1, 1])
que.append([0, 4])

while que:
    temp = que.popleft()
    row = temp[0]
    col = temp[1]
    for i in range(4):
        r = row + dr[i]
        c = col + dc[i]
        if r < 0 or r > 2 or c < 0 or c > 4:
            continue
        if ans[r][c] > 0:
            continue
        ans[r][c] = ans[row][col] + 1
        que.append([r, c])

for j in range(3):
    print(' '.join(map(str, ans[j])))