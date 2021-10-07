#######################################################
# 네 글자를 입력 받는다. ( 중복된 알파벳 선택 가능)
# ex) 'BOTK'
# B와 T가 싸웠다. >> B 와 T는 서로 떨어지도록 자리를 배치

# def my_func(level, path):
#     global cnt
#     if level == 4:
#         cnt += 1
#         return
#     for i in range(4):
#         if path[-1] == 'T' and people[i] == 'B':
#             continue
#         if path[-1] == 'B' and people[i] == 'T':
#             continue
#         my_func(level+1, path+people[i])
#     return
#
#
# people = 'BOTK'
# cnt = 0
# my_func(0, '#')
# print(cnt)

#######################################################
# 네 글자를 입력 받는다. ( 중복된 알파벳 선택 가능)
# ex) 'BOTK'
# B와 T가 싸웠다. >> B 와 T는 서로 떨어지도록 자리를 배치
# 교수님 풀이

# def func(level) :
#     global cnt
#     if level == 4:
#         cnt += 1
#         return
#     for i in range(4):
#         if level > 0 :
#             if path[level - 1] == 'B' and arr[i] == 'T' :continue
#             if path[level - 1] == 'T' and arr[i] == 'B' :continue
#         path[level] = arr[i]
#         func(level + 1)
#         #path[level] = 0
#
#     return
#
# arr = "BOTK"
# path = [0,0,0,0]
# cnt = 0
# func(0)
# print(cnt)

######################################################################
# ABC 초콜릿 중 N개 선택 (중복선택 가능)
# 세개가 연속적으로 선택 x
# ex) AAA : X , BBB : X, ABBBC : X

# def my_func(level, chk, c):
#     global cnt
#     if level == N:
#         cnt += 13
#         return
#     for i in range(3):
#         if chk == arr[i] and c > 1:
#             continue
#         elif chk == arr[i]:
#             my_func(level+1, arr[i], c + 1)
#         else:
#             my_func(level+1, arr[i], 1)
#     return
#
# N = int(input())
# arr = "ABC"
# cnt = 0
# my_func(0, '#', 0)
# print(cnt)


######################################################################
# ABC 초콜릿 중 N개 선택 (중복선택 가능)
# 세개가 연속적으로 선택 x
# ex) AAA : X , BBB : X, ABBBC : X
# 교수님 풀이 - 일단 진입후 백트래킹

# def func(level):
#     global cnt
#     if level >= 3 :
#         if path[level -1] == path[level - 2] and path[level - 2] == path[level - 3] : return # 백트래킹
#     if level == N :
#         cnt += 1
#         return
#     for ch in ['A','B','C']:
#         path[level] = ch
#         func(level + 1)
#         path[level] = 0
#     '''
#     # A
#     path[level] = 'A'
#     func(level + 1)
#     # B
#     path[level] = 'B'
#     func(level + 1)
#     # C
#     path[level] = 'C'
#     func(level + 1)
#     '''
#
#
# N = int(input())
# path = [0] * N
# cnt = 0
# func(0)
# print(cnt)

# 교수님 풀이 - 진입하기전에 가지치기

# def func(level):
#     global cnt
#     if level == N :
#         cnt += 1
#         return
#     for ch in ['A','B','C']:
#         if level >= 2 :
#             if path[level-1] == ch and path[level-2] == ch : continue
#         path[level] = ch
#         func(level + 1)
#         path[level] = 0
#
# N = int(input())
# path = [0] * N
# cnt = 0
# func(0)
# print(cnt)

