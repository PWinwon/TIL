#########################################################
# 0820
#########################################################
# 길찾기 풀이

# def dfs(now):
#     global check
#     if now == -1: return
#     if now == 99:
#         check = 1
#         return
#
#     dfs(left[now])
#     dfs(right[now])
#     return
#
#
# left = [-1 for _ in range(100)]
# right = [-1 for _ in range(100)]
# visited = [0 for _ in range(100)]
#
# N = 16
# lst = list(map(int, input().split()))
# i = 0
# while i < 2 * N:
#     from_, to_ = lst[i], lst[i + 1]
#     if left[from_] == -1:
#         left[from_] = to_
#     else:
#         right[from_] = to_
#     i += 2
#
# check = 0
# dfs(0)  # 99번 노드에 도착할수 있는가?
# if check == 1:
#     print("갈수 있다")
# else:
#     print("갈수 없다")

#########################################################
# 배열 회전 연습
# def shift_lst(a):
#     result = []
#     result.append(a.pop())
#     for i in range(0, len(a)):
#         result.append(a[i])
#     return result
#
#
# lst = [3, 4, 7, 9, 8, 5]
# lst = shift_lst(lst)
# print(lst)
# lst = shift_lst(lst)
# print(lst)

#########################################################
# 배열 회전 연습 - 교수님 풀이

# def rotate(lst):
#     backup = lst[-1]
#     for i in range(4, 0 - 1, -1):
#         lst[i + 1] = lst[i]
#     lst[0] = backup
#
# lst = [3,4,7,9,8,5]
# for i in range(3):
#     rotate(lst)
#     print(lst)

#########################################################
# 배열 회전 연습

# lst = [[3, 2, 1],
#        [5, 5, 5],
#        [7, 6, 5],
#        ]
# copy = []
# for r in range(3):
#     sample = []
#     for c in range(2, -1, -1):
#         sample.append(lst[c][r])
#     copy.append(sample)
#
# print(copy)

#########################################################
# 배열 회전 연습 - 교수님 풀이

# def rotate(MAP):
#     temp = [
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]
#     ]
#     for y in range(3):
#         for x in range(3):
#             temp[x][2 - y] = MAP[y][x]
#     for y in range(3):
#         for x in range(3):
#             MAP[y][x] = temp[y][x]
#     return
#
#
# MAP = [
#     [3,2,1],
#     [5,5,5],
#     [7,6,5]
# ]
# rotate(MAP)
# rotate(MAP)
# rotate(MAP)
# rotate(MAP)
# rotate(MAP)
# rotate(MAP)

#########################################################
# 미로찾기 - 교수님 풀이

# import time
#
# def map_print(ny,nx): # @
#     for i in range(100): print(end = ' ')
#     print()
#     for y in range(7):
#         for x in range(10) :
#             if (y,x) == (ny,nx):
#                 print("@",end='')
#             else :
#                 print(MAP[y][x],end ='')
#         print()
#
#     time.sleep(0.7)
#
# def dfs(y,x):
#     if MAP[y][x] == '#': return
#     if visited[y][x] == 1 : return
#     visited[y][x] = 1
#     map_print(y,x)
#     dfs(y-1,x)
#     map_print(y, x)
#     dfs(y+1,x)
#     map_print(y, x)
#     dfs(y,x-1)
#     map_print(y, x)
#     dfs(y,x+1)
#     map_print(y, x)
#     return
#
# MAP = [
#     "##########",
#     "#_#___#__#",
#     "#_#_#_#_##",
#     "#_#_#_#__#",
#     "#_#_#_#_##",
#     "#___#____#",
#     "##########",
# ]
# visited = [
#     [0 for _ in range(10)] for _ in range(7)
# ]
#
# dfs(1,1)
#########################################################
# 연습문제 - 할아버지가 남긴 땅

# def zero_chk(r1, r2, c1, c2):
#     for r_idx in range(r1, r2+1):
#         for c_idx in range(c1, c2+1):
#             if MAP[r_idx][c_idx] == 0:
#                 return False
#     return True

# def map_sum(r1, r2, c1, c2):
#     my_sum = 0
#     for r_idx in range(r1, r2 + 1):
#         for c_idx in range(c1, c2 + 1):
#             my_sum += MAP[r_idx][c_idx]
#     return my_sum


# test_case = int(input())

# for tc in range(test_case):
#     h, w = map(int, input().split())
#     MAP = [list(map(int, input().split())) for _ in range(h)]

#     max_val = 0
#     for r in range(h):
#         for c in range(w):
#             for row in range(r, h):
#                 for col in range(c, w):
#                     if zero_chk(r, row, c, col):
#                         temp = map_sum(r, row, c, col)
#                         if max_val < temp:
#                             max_val = temp
#     print('#{} {}'.format(tc+1, max_val))

#########################################################
# 연습문제 - 할아버지가 남긴 땅 - 교수님 풀이. 다시풀어보자


# def is_exist(y1,x1,y2,x2):
#     for y in range(y1,y2+1):
#         for x in range(x1,x2+1):
#             if MAP[y][x] == 0: return True
#
#     return False
#
# def get_sum(y1,x1,y2,x2) :
#     sum = 0
#     for y in range(y1,y2+1) :
#         for x in range(x1,x2+1) :
#             sum += MAP[y][x]
#
#     return sum
#
# N,M = map(int , input().split())
# MAP = [
#     list(map(int, input().split())) for _ in range(N)
# ]
#
# max_sum = int(-21e8)
# # 직사각형 잡기
# for y1 in range(0,N):
#     for x1 in range(0,M):
#         # y1,x1
#         for y2 in range(y1, N):
#             for x2 in range(x1, M):
#                 # y2,x2
#                 check = is_exist(y1,x1,y2,x2)
#                 if check == False : # 0이 없음
#                     ret = get_sum(y1,x1,y2,x2)
#                     if max_sum < ret :
#                         max_sum = ret
#
# print(max_sum)

#########################################################
# 버블정렬

# lst = [5, 3, 2, 7, 9, 8, 6]
#
# for i in range(7):
#     for j in range(i, 7):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
#
# print(lst)