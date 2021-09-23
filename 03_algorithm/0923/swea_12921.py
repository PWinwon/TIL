#################################################
# swea 12921 - subtree
# import sys
# sys.stdin = open('0923_input.txt', 'r')
#
#
# def my_func(now):
#     global result
#     result += 1
#     for i in range(1, E+2):
#         if adj[now][i] == 0:
#             continue
#         my_func(i)
#     return
#
#
# test_case = int(input())
#
# for tc in range(test_case):
#     E, N = map(int, input().split())
#     lst = list(map(int, input().split()))
#     adj = [[0 for _ in range(E+2)] for _ in range(E+2)]
#     for e in range(0, 2*E, 2):
#         adj[lst[e]][lst[e+1]] = 1
#     result = 0
#     my_func(N)
#     print('#{} {}'.format(tc+1, result))
#################################################
# swea 12921 - subtree - 교수님풀이

# T = int(input())
#
# def dfs(now) :
#     global cnt
#     if now == 0 : return
#     cnt += 1
#     dfs(adj[now][0]) # 왼쪽 자식
#     dfs(adj[now][1]) # 오른쪽 자식
#
# for tc in range(1, T + 1) :
#     E,N = map(int ,input().split())
#     lst = list(map(int ,input().split()))
#     adj = [[0,0] for _ in range(E + 2)] # 1 ~ E+1 번 노드
#     for i in range(0,len(lst),2):
#         parent = lst[i]
#         child = lst[i + 1]
#         if adj[parent][0] == 0 :
#             adj[parent][0] = child
#         else :
#             adj[parent][1] = child
#     cnt = 0
#     dfs(N)
#     print("#{} {}".format(tc, cnt))