# def my_func(level, now, total):
#     global result
#     if result < total:
#         return
#     if level == N-1:
#         total += adj[now][0]
#         if result > total:
#             result = total
#         return
#     for i in range(N):
#         if adj[now][i] == 0:
#             continue
#         if used[i] == 1:
#             continue
#         used[i] = 1
#         my_func(level+1, i, total + adj[now][i])
#         used[i] = 0
#     return
#
#
# T = int(input())
#
# for tc in range(T):
#     N = int(input())
#     adj = [list(map(int, input().split())) for _ in range(N)]
#     used = [0] * N
#     used[0] = 1
#     result = 9999999
#     my_func(0, 0, 0)
#     print('#{} {}'.format(tc+1, result))


##########################################################################
# 교수님 풀이

import sys
sys.stdin = open("text.txt", "r")

T = int(input())

def dfs(now, cost, cnt, path) : # 현재 노드 , 현재 누적 비용
    global min_cost
    if cnt == N : # 모든 노드들을 방문함
        if adj[now][0] > 0 :
            min_cost = min(min_cost , cost + adj[now][0])
        return
    # next 찾기
    for next in range(N) :
        if adj[now][next] == 0 : continue
        if visited[next] == 1: continue
        visited[next] = 1
        dfs(next,cost + adj[now][next], cnt + 1, path + str(next))
        visited[next] = 0

for tc in range(1, T + 1) :
    N = int(input())
    adj = [
        list(map(int, input().split())) for _ in range(N)
    ]
    visited = [0] * N

    min_cost = int(21e8)
    visited[0] = 1
    dfs(0,0,1, "0")
    print("#{} {}".format(tc, min_cost))