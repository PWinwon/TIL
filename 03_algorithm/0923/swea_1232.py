#################################################
# swea 1232 - Daily과제 - 사칙연산

# import sys
# sys.stdin = open('0923_input.txt', 'r')
#
#
# def my_func(level):
#     if level > N+1:
#         return
#     if type(lst[level]) != list:
#         return
#     my_func(int(lst[level][1]))
#     my_func(int(lst[level][2]))
#     if lst[level][0] == '+':
#         lst[level] = lst[int(lst[level][1])] + lst[int(lst[level][2])]
#     elif lst[level][0] == '-':
#         lst[level] = lst[int(lst[level][1])] - lst[int(lst[level][2])]
#     elif lst[level][0] == '*':
#         lst[level] = lst[int(lst[level][1])] * lst[int(lst[level][2])]
#     elif lst[level][0] == '/':
#         lst[level] = lst[int(lst[level][1])] / lst[int(lst[level][2])]
#     return
#
#
# for tc in range(1, 11):
#     N = int(input())
#     lst = [0] * (N+1)
#     for i in range(N):
#         temp = list(input().split())
#         if len(temp) == 2:
#             lst[int(temp[0])] = int(temp[1])
#         else:
#             lst[int(temp[0])] = temp[1:4]
#     my_func(1)
#     print('#{} {}'.format(tc, int(lst[1])))