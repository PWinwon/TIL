#################################################
# swea 12922 - 이진탐색

# import sys
# sys.stdin = open('0923_input.txt', 'r')
#
#
# def my_func(now):
#     global cnt
#     if now > N:
#         return
#     my_func(now*2)
#     lst[now] = cnt
#     cnt += 1
#     my_func(now*2+1)
#     return
#
#
# test_case = int(input())
#
#
# for tc in range(test_case):
#     N = int(input())
#     lst = [0] * (N+1)
#     cnt = 1
#     my_func(1)
#     print('#{} {} {}'.format(tc+1, lst[1], lst[N//2]))