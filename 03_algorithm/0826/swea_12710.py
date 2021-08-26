test_case = int(input())

for tc in range(test_case):
    V, E = map(int, input().split())
    adj = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        idx1, idx2 = map(int, input().split())
        adj[idx1][idx2] = 1
        adj[idx2][idx1] = 1
    S, G = map(int, input().split())
    used = [0] * (V+1)
    que = [0] * (V+1)
    que[0] = S
    front = 0
    rear = 1
    while front < rear:
        temp = que[front]
        if used[G]:
            break
        for i in range(1, V+1):
            if adj[temp][i] == 1 and used[i] == 0:
                que[rear] = i
                used[i] = used[temp] + 1
                rear += 1
        front += 1
    print('#{} {}'.format(tc+1, used[G]))

#############################################################
# 교수님 풀이

# temp = int(input())
#
# from collections import deque
#
# def bfs(start, goal)  :
#     level = [0 for _ in range(N+1)] # level[노드번호] 몇회만에 이동했는지 저장
#     visited = [0 for _ in range(N+1)] # visited[노드번호] queue 에 재등록 방지 처리
#     queue = deque()
#     queue.append(start)
#     visited[start] = 1
#     level[start] = 0  # 0회
#
#     while queue :
#         now = queue.popleft()
#         # 탐색 및 처리
#         if now == goal : return level[now]
#         for next in range(1,N+1):
#             if adj[now][next] == 0 : continue
#             if visited[next] == 1 : continue
#             visited[next] = 1
#             level[next] = level[now] + 1
#             queue.append(next)
#
#     return -1
#
#
#
#
# for tc in range(1,temp+1) :
#     N,T = map(int,input().split()) # [1~N]
#     adj = [ # N+1 by N+1
#         [0 for _ in range(N+1)] for _ in range(N+1)
#     ]
#     for _ in range(T):
#         a,b = map(int,input().split())
#         adj[a][b] = 1
#         adj[b][a] = 1
#     S,G = map(int,input().split()) # 시작 노드 / 도착 노드
#     # 구하고자 하는것은 S~G로의 최소 이동 횟수
#     ret = bfs(S,G)
#     if ret == -1 :
#         print(0)
#     else :
#         print(ret)