#######################################################
# 주사위 n개를 던져서 나올 수 있는 모든 경우 출력

# def my_func(level, dice):
#     if level == N:
#         print(dice)
#         return
#     for i in range(1, 7):
#         dice[level] = i
#         my_func(level+1, dice)
#     return
#
#
# N = int(input())
# path = [0] * N
# my_func(0, path)


#######################################################
# 주사위 n개를 던져서 나올 수 있는 모든 경우 출력 - 교수님 풀이

# def func(level) :
#     if level == N :  # 0 1 2 3 ... N -1 / (총 N개 선택 ) N
#         # 하나의 경우의 수가 만들어짐
#         for i in range(N) :
#             print(path[i],end = '' )
#         print()
#         return
#
#     for i in range(1, 6 + 1):
#         path[level] = i # 현재 level 에서 i 눈금 선택 후 ,
#         func(level + 1)
#         path[level] = 0 # 원상복구
#
#
# N = int(input())
# path = [0,0,0,0,0,0,0,0,0,0,]
# func(0)

#######################################################
# 주사위 n개를 던져서 나올 수 있는 모든 경우 중 중복없이 출력

# def my_func(level, dice):
#     if level == N:
#         print(dice)
#         return
#     for i in range(1, 7):
#         if used[i] == 1:
#             continue
#         used[i] = 1
#         dice[level] = i
#         my_func(level+1, dice)
#         used[i] = 0
#     return


# N = int(input())
# path = [0] * N
# used = [0] * 7
# my_func(0, path)

#######################################################
# 선택정렬 재귀적 알고리즘

# def my_func(level):
#     if level == 10:
#         print(lst)
#         return
#     min_idx = level
#     for i in range(level, 10):
#         if lst[min_idx] > lst[i]:
#             min_idx = i
#     lst[level], lst[min_idx] = lst[min_idx], lst[level]
#     my_func(level+1)
#     return
#
#
# lst = [9, 5, 4, 6, 1, 3, 15, 7, 2, 0]
# my_func(0)

#######################################################
# 선택정렬 재귀적 알고리즘 - 교수님 풀이

# def selection_sort(s,e):
#     if s == e :
#         return
#     # [s] <- 에 제일 작은 값을 swap
#     min_idx = s
#     for i in range(s,e+1):
#         if arr[min_idx] > arr[i] :
#             min_idx = i
#     arr[min_idx], arr[s] = arr[s] , arr[min_idx]
#
#     selection_sort(s + 1, e)
#
#
# arr = [1,3,2,5,6,30,22,19]
# selection_sort(0,len(arr) - 1)
# print(arr)

#######################################################
# 부분집합

# def my_func(level):
#     global cnt
#     if level == 5:
#         for i in range(5):
#             if path[i] == 0:
#                 continue
#             print(path[i], end=' ')
#         print('')
#         cnt += 1
#         return
#     path[level] = lst[level]
#     my_func(level+1)
#     path[level] = 0
#     my_func(level+1)
#     return
#
#
# lst = [1, 2, 3, 5, 9]
# path = [0, 0, 0, 0, 0]
# cnt = 0
# my_func(0)
# print(cnt)

#######################################################
# 부분집합 - 교수님 풀이

# def func(level):
#     global cnt
#     if level == 5:
#         print(subset)
#         cnt += 1
#         return
#
#     subset.append(arr[level])
#     func(level + 1) # 현재 level 원소 선택 O
#     subset.pop()
#
#     func(level + 1) # 현재 level 원소 선택 X
#
#
# subset = []
# arr = [1,3,5,7,9]
#
# cnt = 0
# func(0)

# def func(level):
#     global cnt
#     if level == 10:
#         #print(subset)
#         #cnt += 1
#         sum = 0
#         for i in range(len(subset)):
#             sum += subset[i]
#         if sum == 0 :
#             cnt += 1
#         return
#
#     subset.append(arr[level])
#     func(level + 1) # 현재 level 원소 선택 O
#     subset.pop()
#
#     func(level + 1) # 현재 level 원소 선택 X
#
#
# subset = []
# arr = [-1,3,-9,6,7,-6,1,5,4,-2]
#
# cnt = 0
# func(0)
# print(cnt)



