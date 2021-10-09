# def quick_sort(s, e):
#     if s > e:
#         return
#     pvt = lst[s]
#     s_idx = s + 1
#     e_idx = e
#     while s_idx <= e_idx:
#         if lst[s_idx] <= pvt:
#             s_idx += 1
#         elif lst[e_idx] > pvt:
#             e_idx -= 1
#         else:
#             lst[s_idx], lst[e_idx] = lst[e_idx], lst[s_idx]
#     lst[s], lst[e_idx] = lst[e_idx], lst[s]
#     quick_sort(s, e_idx - 1)
#     quick_sort(e_idx + 1, e)
#     return
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     quick_sort(0, N - 1)
#     print('#{} {}'.format(tc, lst[N // 2]))

#######################################################################
# 교수님 풀이


# def partition(s, e, lst):
#     pi = s
#     small = s + 1
#     big = e
#     while small <= big:
#         while small <= big and lst[pi] >= lst[small]:  # 작은값 영역 넓히기  small ->
#             small += 1
#         while small <= big and lst[pi] <= lst[big]:  # 큰값 영역 넓히기 <- big
#             big -= 1
#         if small < big:
#             lst[small], lst[big] = lst[big], lst[small]  # swap
#     lst[pi], lst[big] = lst[big], lst[pi]
#     return big
#
#
# def quick_sort(s, e, lst):
#     if s > e: return
#     pivot = partition(s, e, lst)  # 파티션하고 / pivot의 인덱스 return 받기
#     quick_sort(s, pivot - 1, lst)
#     quick_sort(pivot + 1, e, lst)
#     return
#
#
# lst = list(map(int, input().split()))
# quick_sort(0, len(lst) - 1, lst)