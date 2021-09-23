#################################################
# 0923
#################################################
# 트리 복습(중위순회 - 하드코딩)
# 인덱스 이용한 풀이
# 교수님 : 인덱스를 이용한 풀이에서 리스트의 구성은 비어있는 값에 대해 공집합 처리를 해주어야함 (나는 0으로 표시)
# 그래서 편향된 이진트리 구조의 문제에 대해서는 메모리가 낭비될 가능성이 매우 큼
# 문제에 따라 방법을 달리하여 풀어야함

# def my_func(level):
#     if level > 9:
#         return
#     if lst[level] == 0:
#         return
#     my_func(2 * level)
#     print(lst[level], end=' ')
#     my_func(2 * level + 1)
#     return
#
#
# lst = [0, 'A', 'B', 'C', 'D', 'E', 0, 'F', 'G', 'H', 'I']
# my_func(1)

#################################################
# 트리 복습(중위순회 - 하드코딩) 교수님풀이
# left와 right 배열을 이용한 풀이

# def dfs(now):
#     if now == -1:
#         return
#     dfs(left[now]) # left subtree
#     print(now, end=' ')
#     dfs(right[now]) # right subtree
#     return
#
#
# left = [-1 for _ in range(9)]
# right = [-1 for _ in range(9)]
#
# left[0] = 1
# right[0] = 2
#
# left[1] = 3
# right[1] = 4
#
# left[2] = 5
# right[2] = 6
#
# left[3] = 7
# right[3] = 8
#
# dfs(0)

#################################################
# 트리 복습(중위순회 - 하드코딩)
# 인접리스트를 이용한 풀이
# def dfs(now):
#     if adj[now][0] != -1:
#         dfs(adj[now][0])
#     print(now, end=' ')
#     if adj[now][1] != -1:
#         dfs(adj[now][1])
#     return
#
#
# adj = [[-1, -1] for _ in range(9)]
#
# adj[0][0] = 1
# adj[0][1] = 2
# adj[1][0] = 3
# adj[1][1] = 4
# adj[2][0] = 5
# adj[2][1] = 6
# adj[3][0] = 7
# adj[3][1] = 8
#
# dfs(0)




#################################################
# 힙 insert 구현해보기 - 교수님 풀이

# tree = [0]
#
# lst = [3,2,5,7,1,0,7]
#
# for i in range(len(lst)):
#     tree.append(lst[i]) # 맨 마지막에 놓기
#     # 자기자리 찾기 ( 자기자리 찾을때까지 swap 하기 )
#     now = len(tree) - 1
#     parent = now // 2
#     # 자기자리 찾기
#     # [parent] vs [now]  ,   parent <= now 이도록 유지 -> 만약에 parent > now 일때 swap 하기
#     while now > 1 and tree[parent] > tree[now]:
#         tree[parent], tree[now] = tree[now] , tree[parent] # swap
#         now = parent
#         parent = now // 2
#
#     de = -1


#################################################
# BFS 경로 찾기 리마인드
# from collections import deque
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# MAP = [
#     "#########",
#     "#S#_____#",
#     "#_#_##E##",
#     "#___#___#",
#     "#_______#",
#     "#########",
# ]
#
# used = [[0 for _ in range(8)] for _ in range(6)]
# que = deque()
# start = [1, 1]
# end = [2, 6]
# que.append(start)
# used[1][1] = 1
# while que:
#     temp = que.popleft()
#     row = temp[0]
#     col = temp[1]
#     if row == end[0] and col == end[1]:
#         result = used[row][col]
#         break
#     for i in range(4):
#         r = row + dr[i]
#         c = col + dc[i]
#         if MAP[r][c] == '#':
#             continue
#         if used[r][c] > 0:
#             continue
#         used[r][c] += used[row][col] + 1
#         que.append([r, c])
# print(result)

#################################################
# BFS 경로 찾기 리마인드 - 교수님 풀이
#
# MAP = [
#     "#########",
#     "#S#_____#",
#     "#_#_##E##",
#     "#___#___#",
#     "#_______#",
#     "#########",
# ]
#
# from collections import deque
#
# queue = deque()
# visited = [[0 for _ in range(len(MAP[0]))] for _ in range(len(MAP))] # 큐에 다시 등록 못하도록 (+ level을 기록해도 됬음)
#
# visited[1][1] = 1
# queue.append((1,1,0)) # (y,x ) 시작좌표, level  : 0 -> 0회만에 (1,1) 도착
#
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
# # bfs 시작
# while queue : # queue 에 방문 예약이 있다
#     y,x,level = queue.popleft()
#     # 탐색 코드 작성하기
#     if MAP[y][x] == 'E':
#         print(level)
#         break
#     for t in range(4) :
#         ny = y + dy[t]
#         nx = x + dx[t]
#         if MAP[ny][nx] == '#' : continue
#         if visited[ny][nx] == 1 : continue
#         visited[ny][nx] = 1 # 큐에 등록함
#         queue.append((ny,nx,level + 1))

