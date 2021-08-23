#############################################################
# 0823
#############################################################
# 후위 표기법 연습

# expression = '12312312312'
# e_len = 9
# idx = 0
# result = 'success'
# while idx < e_len - 1:
#     if expression[idx] == '1' and expression[idx+1] == '2':
#         idx += 1
#         continue
#     elif expression[idx] == '2' and expression[idx+1] == '3':
#         idx += 1
#         continue
#     elif expression[idx] == '3' and expression[idx+1] == '1':
#         idx += 1
#         continue
#     result = 'fail'
#     break
#
# print(result)


#############################################################
# 후위 표기법 연습  - 교수님 풀이

# def is_valid(left, right):
#     if left == '1' and right != '2' : return False
#     if left == '2' and right != '3' : return False
#     if left == '3' and right != '1' : return False
#     return True
#
# s = "1231212312"
# check = 0
# for i in range(0, len(s) - 1) :
#     ret = is_valid(s[i],s[i+1])
#     if ret == False :
#         check = 1
#
# if check == 0 :
#     print("O")
# else :
#     print("X")


#############################################################
# 후위 표기법

# order_calc = {
#     '(': 0,
#     '+': 1,
#     '-': 1,
#     '*': 2,
#     '/': 2,
# }
#
# test_case = int(input())
#
# for tc in range(test_case):
#     e = input().rstrip()
#     e_len = len(e)
#     stk = []
#     result = ''
#     idx = 0
#     while idx < e_len:
#         if e[idx].isdigit():
#             result += e[idx]
#         elif e[idx] == '(':
#             stk.append(e[idx])
#         elif e[idx] == ')':
#             while stk != [] and stk[-1] != '(':
#                 result += stk.pop()
#             stk.pop()
#         elif stk == [] or order_calc[e[idx]] > order_calc[stk[-1]]:
#             stk.append(e[idx])
#         else:
#             while stk != [] and order_calc[e[idx]] <= order_calc[stk[-1]]:
#                 result += stk.pop()
#             stk.append(e[idx])
#         idx += 1
#
#     while stk:
#         result += stk.pop()
#
#     print('#{} {}'.format(tc+1, result))

#############################################################
# 후위 표기법 - 교수님 풀이

# def is_valid(s1 ,s2) : # s1 > s2 인지?
#     eval = {'+':1,'-':1,'*':2,'/':2,'(':0}
#     if eval[s1] > eval[s2] : return True
#     else : return False
#
#
# s = input().rstrip()
# stack = [] # 연산자
# n = len(s)
# i = 0
# result = ''
# while i < n :
#     # s[i] -> 숫자다
#     # s[i] ==  '('
#     # s[i] == ')' 여는괄호부터 닫는 괄호 사이에
#     # 나머지 연산자들은 우선순위에 따라서 처리
#
# print(result)

#############################################################
# 백트래킹 연습
# import time
# import os
#
# def map_print(nr, nc, type):
#     os.system('cls')
#     for y in range(7):
#         for x in range(10):
#             if (nr, nc) == (y, x) and type == -1:
#                 print('X', end='')
#             elif (nr, nc) == (y, x) and type == 0:
#                 print('@', end='')
#             else:
#                 print(MAP[y][x], end='')
#         print('')
#     time.sleep(0.5)
#
#
# #        상, 하, 좌, 우
# dir_r = [-1, 1, 0, 0]
# dir_c = [0, 0, -1, 1]
#
# def miro_tracking(r, c):
#     if MAP[r][c] == '#':
#         map_print(r,c,-1)
#         return
#     if visited[r][c] == 1:
#         map_print(r,c,-1)
#         return
#     visited[r][c] = 1
#     for idx in range(4):
#         map_print(r, c, 0)
#         miro_tracking(r+dir_r[idx], c+dir_c[idx])
#         map_print(r, c, 0)
#     return
#
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
# miro_tracking(1, 1)

#############################################################
# 백트래킹 연습 - 교수님 풀이
# import time
# import os
#
# def map_print(ny,nx, type ):
#     os.system("cls")
#     for y in range(7):
#         for x in range(10):
#             if (ny,nx) == (y,x) and type == -1 :
#                 print("X",end='')
#             elif (ny,nx) == (y,x) and type == 0:
#                 print("@",end='')
#             else :
#                 print(MAP[y][x],end='')
#         print()
#
#     time.sleep(0.5)
#
#
# def dfs(y,x):
#     if MAP[y][x] == '#':
#         map_print(y,x,-1)
#         return # 가지치기 (이후의 재귀호출을 제거)
#     if visited[y][x] == 1:
#         map_print(y,x,-1)
#         return # 가지치기 (이후의 재귀호출을 제거)
#
#     visited[y][x] = 1
#     map_print(y,x,0)
#     dfs(y-1,x) #위
#     map_print(y, x, 0)
#     dfs(y+1,x) #아래
#     map_print(y, x, 0)
#     dfs(y,x-1) #왼쪽
#     map_print(y, x, 0)
#     dfs(y,x+1) #오른쪽
#     map_print(y, x, 0)
#     return
#
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
#
# visited = [
#     [0 for _ in range(10)] for _ in range(7)
# ]
#
# dfs(1,1)

#############################################################
# N Castle

# def chess_chk(a, n):
#     global cnt
#     if a == n:
#         cnt += 1
#         return
#     for j in range(n):
#         if visited[j] == 1:
#             continue
#         visited[j] = 1
#         chess_chk(a+1, n)
#         visited[j] = 0
#     return
#
# for tc in range(1, 11):
#     N = int(input())
#     cnt = 0
#     visited = [0 for _ in range(N)]
#     chess_chk(0, N)
#     print('#{} {}'.format(tc, cnt))

#############################################################
# N Castle - 백트래킹

# def map_print():
#     for r in range(3):
#         for c in range(3):
#             print(MAP[r][c], end=' ')
#         print('')
#     print('--------------------------')
#
# def dfs(level):
#     if level == 3:
#         map_print()
#         return
#     for i in range(3):
#         if visited[i] == 1:
#             continue
#         visited[i] = 1
#         MAP[level][i] = '#'
#         dfs(level + 1)
#         visited[i] = 0
#         MAP[level][i] = '_'
#     return
#
#
# MAP = [
#     ['_', '_', '_'],
#     ['_', '_', '_'],
#     ['_', '_', '_'],
# ]
# visited = [0] * 3
# dfs(0)

#############################################################
# N Castle - 백트래킹 - 교수님 풀이

# def dfs(level):
#     # 현재 level 에서 선택할수 있는 x 좌표는 0 1 2
#     if level == 3 :
#         de = - 1
#         return
#     for x in range(3):
#         if used[x] == 1 :
#             continue
#         MAP[level][x] = '#'
#         used[x] = 1 # x좌표 사용(이후의 재귀호출에서 재사용 방지)
#         dfs(level+1)
#         used[x] = 0 # 원상복구
#         MAP[level][x] = '_'
#
#     return
#
#
# MAP = [
#     ['_','_','_'],
#     ['_','_','_'],
#     ['_','_','_'],
# ]
# used = [0,0,0] # 0 1 2 의 사용 여부
# dfs(0)

#############################################################
# 부분집합의 합 2

# def part_sum(i, n, total, RS):
#     global cnt
#     if n == N:
#         if total == K:
#             cnt += 1
#         return
#     if total > K:
#         return
#     if (total + RS) < K:
#         return
#     if i > 20:
#         return
#     part_sum(i+1, n+1, total+i+1, RS-i-1)
#     part_sum(i+1, n, total, RS-i)
#
# test_case = int(input())
#
# max_val = 210
#
# for tc in range(test_case):
#     N, K = map(int, input().split())
#     cnt = 0
#     part_sum(0, 0, 0, max_val)
#     print('#{} {}'.format(tc+1, cnt))

#############################################################
# 계산기 2

# order_val = {
#     '+': 1,
#     '*': 2
# }
#
# for tc in range(1, 11):
#     n = int(input())
#     expr = input()
#     back_e = []
#     stack = []
#     idx = 0
#     while idx < n:
#         if expr[idx].isdigit():
#             back_e.append(expr[idx])
#         elif stack == [] or (order_val[expr[idx]] >= order_val[stack[-1]]):
#             stack.append(expr[idx])
#         else:
#             while stack != [] and order_val[expr[idx]] <= order_val[expr[idx]]:
#                 back_e.append(stack.pop())
#             stack.append(expr[idx])
#         idx += 1
#
#     while stack:
#         back_e.append(stack.pop())
#
#     num_stack = []
#     idx = 0
#     while idx < n:
#         if back_e[idx].isdigit():
#             num_stack.append(ord(back_e[idx]) - ord('0'))
#         elif back_e[idx] == '*':
#             a = num_stack.pop()
#             b = num_stack.pop()
#             num_stack.append(b*a)
#         else:
#             a = num_stack.pop()
#             b = num_stack.pop()
#             num_stack.append(b+a)
#         idx += 1
#
#     print('#{} {}'.format(tc, num_stack[0]))
