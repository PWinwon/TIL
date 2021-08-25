###################################################
# bfs 연습 (인접행렬 하드 코딩 후 자식노드 값 출력하기)

# value = [0, 1, 1, 3, 2, 4, 5, 2]
# arr = [
#     [0, 1, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]
#
# N = int(input())
#
# for idx in range(8):
#     if arr[N][idx] == 1:
#         print(value[idx], end=' ')

###################################################
# bfs 교수님 풀이

# value = [0,1,1,3,2,4,5,2]
# adj = [
#     [0 for _ in range(8)] for _ in range(8)
# ]
#
# # from -> to [from][to]
# adj[0][1] = 1
# adj[0][2] = 1
# adj[0][3] = 1
# adj[1][4] = 1
# adj[1][5] = 1
# adj[1][6] = 1
# adj[3][7] = 1
#
# # 자식 노드의 값을 출력
# now = int(input())
# for next in range(8):
#     if adj[now][next] == 1: # next 가 자식노드
#         print(value[next],end=' ')

###################################################
# 큐를 활용한 bfs 연습

# from collections import deque
#
# value = [0, 1, 1, 3, 2, 4, 5, 2]
# arr = [
#     [0, 1, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]
#
# que = deque()
# que.append(0)
# while que:
#     print(que)
#     temp = que.popleft()
#     for i in range(8):
#         if arr[temp][i] == 1:
#             que.append(i)


###################################################
# 큐를 활용한 bfs 연습 - 교수님 풀이


# from collections import deque
#
# value = [0,1,1,3,2,4,5,2]
# adj = [
#     [0 for _ in range(8)] for _ in range(8)
# ]
# # from -> to [from][to]
# adj[0][1] = 1
# adj[0][2] = 1
# adj[0][3] = 1
# adj[1][4] = 1
# adj[1][5] = 1
# adj[1][6] = 1
# adj[3][7] = 1
#
# queue = deque()
#
# # 0 번노드의 자식노드 큐등록
# for next in range(8):
#     if adj[0][next] == 1:
#         queue.append(next)
# de = -1
#
# # 큐에서 하나 뽑아서 그 자식노드를 큐등록
# now = queue.popleft()
# for next in range(8):
#     if adj[now][next] == 1 :
#         queue.append(next)

###################################################
# 큐를 활용한 bfs 연습 - 교수님 풀이 2

# from collections import deque
#
# value = [0,1,1,3,2,4,5,2]
# adj = [
#     [0 for _ in range(8)] for _ in range(8)
# ]
# # from -> to [from][to]
# adj[0][1] = 1
# adj[0][2] = 1
# adj[0][3] = 1
# adj[1][4] = 1
# adj[1][5] = 1
# adj[1][6] = 1
# adj[3][7] = 1
#
# queue = deque()
# queue.append(0) # 시작노드 큐등록
#
# #BFS
# while queue : # 방문 예약 있다!
#     now = queue.popleft()
#     # 방문 / 탐색
#     print(now, end = ' ')
#
#     for next in range(8):
#         if adj[now][next] == 1:
#             queue.append(next) ## 자식노드 찾아서 큐등록(방문예약 )

###################################################
# 큐를 활용한 bfs 연습 - 2

# from collections import deque
#
# value = [0, 1, 1, 3, 2, 4, 5, 2]
# arr = [
#     [0, 1, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]
#
# que = deque()
# que.append(0)
# while que:
#     temp = que.popleft()
#     print(value[temp], end=' ')
#     for i in range(8):
#         if arr[temp][i] == 1:
#             que.append(i)

###################################################
# 그래프 구조 큐를 활용한 bfs

# from collections import deque
#
# que = deque()
#
# arr = [[0 for _ in range(5)] for _ in range(5)]
#
# arr[0][1] = 1
# arr[0][2] = 1
# arr[1][3] = 1
# arr[1][4] = 1
# arr[2][1] = 1
# arr[2][3] = 1
# arr[4][2] = 1
#
# visited = [0] * 5
# que.append(0)
# visited[0] = 1
#
# while que:
#     temp = que.popleft()
#     print('{} 의 level은 : {}'.format(temp, visited[temp]))
#     for i in range(5):
#         if arr[temp][i] == 0:
#             continue
#         if visited[i] > 0:
#             continue
#         visited[i] = visited[temp] + 1
#         que.append(i)








