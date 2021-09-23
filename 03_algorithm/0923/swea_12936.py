#################################################
# swea 12936 - 이진힙

# import sys
# sys.stdin = open('0923_input.txt', 'r')
#
# # heapq 써서 풀기
#
# import heapq
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     result = []
#     for n in range(N):
#         heapq.heappush(result, lst[n])
#     res = 0
#     result = [0] + result
#     N = N
#     while N > 0:
#         N = N // 2
#         res += result[N]
#     print('#{} {}'.format(tc+1, res))


# heapq 안쓰고 풀기
# test_case = int(input())
#
# for tc in range(test_case):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     result = [0]
#     idx = 0
#     while idx < N:
#         temp = lst[idx]
#         idx += 1
#         result.append(temp)
#         cnt = idx
#         while True:
#             if result[cnt//2] > result[cnt]:
#                 result[cnt//2], result[cnt] = result[cnt], result[cnt//2]
#                 cnt = cnt // 2
#             else:
#                 break
#     res = 0
#     while N > 0:
#         N = N // 2
#         res += result[N]
#     print('#{} {}'.format(tc+1, res))


#################################################
# swea 12936 - 이진힙 - 교수님 풀이

# def insert_heap (val):
#     tree.append(val)
#     now = len(tree) - 1
#     parent = now // 2
#     # 자기자리 찾기
#     while now > 1 and tree[parent] > tree[now]:
#         # swap
#         tree[parent], tree[now]  = tree[now], tree[parent]
#         # now 를 갱신
#         now = parent
#         parent = now // 2
#
#
#
#
# T = int (input())
# for tc in range(1, T +1) :
#     N = int(input())
#     lst = list(map(int, input().split()))
#     tree = [0]
#     for val in lst :
#         insert_heap(val)
#
#     # 마지막 노드의 조상노드 전부 더하기 (조상노드 : root ~ 현재 노드까지의 경로상에 있는 모든 노드들)
#     now = len(tree) - 1
#     now //= 2
#     parent = now // 2
#     sum = 0
#     while now != 0 :
#         sum += tree[now]
#         now //= 2
#     print("#{} {}".format(tc, sum))