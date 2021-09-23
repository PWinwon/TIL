#################################################
# swea 12937 - 노드의 합

# import sys
# sys.stdin = open('0923_input.txt', 'r')
#
#
# def my_func(level):
#     if level > N:
#         return 0
#     if lst[level] != 0:
#         return lst[level]
#     a = my_func(level*2)
#     b = my_func(level*2+1)
#     lst[level] = a + b
#     return lst[level]
#
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N, M, L = map(int, input().split())
#     lst = [0] * (N+1)
#     for m in range(M):
#         m_idx, m_val = map(int, input().split())
#         lst[m_idx] = m_val
#     my_func(L)
#     print('#{} {}'.format(tc+1, lst[L]))

#################################################
# swea 12937 - 노드의 합 - 교수님 풀이 tree에 값 변화

# T = int(input())
#
# def dfs(idx) :
#     if idx > N : return
#     if tree[idx] > 0 : return
#     dfs(idx * 2) # left subtree 값 채우기
#     dfs(idx * 2 + 1) # right subtree 값 채우기
#
#     # tree[idx]= tree[idx * 2 ] + tree[idx * 2 + 1]
#     if idx * 2 <= N : tree[idx] += tree[idx * 2]
#     if idx * 2 + 1 <= N : tree[idx] += tree[idx * 2 + 1]
#
#
#
# for tc in range(1, T + 1) :
#     N,M,L = map(int, input().split())
#     tree = [0] * (N + 1)
#     for i in range(M):
#         a,b = map(int, input().split())
#         tree[a] = b
#
#     dfs(1)
#     print("#{} {}".format(tc, tree[L]))

#################################################
# swea 12937 - 노드의 합 - 교수님 풀이 return에 값 넘겨주기

# T = int(input())
#
# def dfs(idx) :
#     if idx > N : return 0
#     if tree[idx] > 0 : return tree[idx]
#     a = dfs(idx * 2) # left subtree 값 채우기
#     b = dfs(idx * 2 + 1) # right subtree 값 채우기
#     tree[idx] = a + b
#     return tree[idx]
#
#
#
#
#
# for tc in range(1, T + 1) :
#     N,M,L = map(int, input().split())
#     tree = [0] * (N + 1)
#     for i in range(M):
#         a,b = map(int, input().split())
#         tree[a] = b
#
#     dfs(1)
#     print("#{} {}".format(tc, tree[L]))

#################################################
# swea 12937 - 노드의 합 - 교수님 풀이 (dp)
# T = int(input())
#
# for tc in range(1, T + 1) :
#     N,M,L = map(int, input().split())
#     dp = [0] * ( N + 1 )
#     num = int(21e8)
#     for i in range(M):
#         a,b = map(int, input().split())
#         dp[a] = b
#         num = min(num, a)
#
#     for i in range(num - 1, 1-1, -1):
#         if i * 2 + 1 <= N :
#             dp[i] = dp[i * 2] + dp[i * 2 + 1]
#         else :
#             dp[i] = dp[i * 2]
#     print("#{} {}".format(tc, dp[L]))