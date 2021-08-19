#########################################################
# 0819
#########################################################
# 몸풀기 - 재귀함수와 trace

# def test(n):
#     print(lst[n], end=' ')
#     if n == 5:
#         return
#     test(n+1)
#     print(lst[n], end=' ')
#     return
#
# lst = [3, 5, 7, 9, 10, 6]
# test(0)

#########################################################
# 몸풀기2 - 재귀함수와 trace

# def func(lev):
#     global a
#     if lev == 3:
#         print(a, end=' ')
#         a += 1
#         return
#     print('#', end=' ')
#     func(lev + 1)
#     func(lev + 1)
#     print('@', end=' ')
#     return
# a = 1
# func(0)

#########################################################
# 몸풀기3 - 재귀함수와 trace
# def func(lev, s):
#     if lev == 2:
#         print(s)
#         return
#     func(lev + 1, s + 'L')
#     func(lev + 1, s + 'M')
#     func(lev + 1, s + 'R')
#     return
#
# func(0,'')

#########################################################
# 몸풀기4 - 재귀함수와 trace(경우의 수)

# def path_cnt(n, s):
#     global cnt
#     if n == 3:
#         cnt += 1
#         print(s)
#         return
#     path_cnt(n+1, s + '1')
#     path_cnt(n+1, s + '2')
#     path_cnt(n+1, s + '3')
#     return
# 
# cnt = 0
# path_cnt(0, '')
# print(cnt)

#########################################################
# 몸풀기5 - 재귀함수와 trace(주사위 경우의수)

# def get_dice(level,path): # 현재 level 주사위에서 선택할수 있는 가지가 6개
#     global n
#     if level == n:
#         print(path)
#         return
#     for i in range(1,6+1):
#         get_dice(level+1,path+str(i))
#
#
# n = int(input())
# get_dice(0,"")

#########################################################
# 몸풀기5 - 재귀함수와 trace(구간의 합 구하기) 1~10

# def func(now):
#     if now == 1:
#         return 1
#     ret = func(now-1)
#     return now + ret
#
#
# print(func(10))

#########################################################
# 종이 붙이기

# def paper_cnt(h, c):
#     global cnt
#     if h >= 10:
#         paper_cnt(h - 10, c)
#     if h >= 20:
#         c *= 2
#         paper_cnt(h - 20, c)
#     if h == 0:
#         cnt += c
#         return

# def paper_cnt(h):
#     if h == 10:
#         return 1
#     if h == 20:
#         return 3
#     return paper_cnt(h - 10) + 2 * paper_cnt(h - 20)
#
#
#
# test_case = int(input())
#
# for tc in range(test_case):
#     height = int(input())
#     cnt = 0
#     cnt = paper_cnt(height)
#     print('#{} {}'.format(tc+1, cnt))

#########################################################
# 종이 붙이기 - 교수님 풀이

# def func(n) :
#     if n == 10 : return 1
#     if n == 20 : return 3
#
#     a = func(n-10) # |
#     b = func(n-20) # = ㅁ
#
#     ret = a + b * 2
#     return ret
#
# ret = func(70)
# print(ret)


# def func(n):  # dp용 x
#     global cnt
#     if n > goal:
#         return
#     if n == goal:
#         cnt += 1
#         return
#     func(n + 10)  # |
#     func(n + 20)  # =
#     func(n + 20)  # ㅁ
#
#
# cnt = 0
# goal = int(input())
# func(0)
# print(cnt)

#########################################################
# 괄호 검사

# test_case = int(input())
#
# for tc in range(test_case):
#     str_chk = input()
#     stk = []
#     result = 1
#     for idx in range(len(str_chk)):
#         if str_chk[idx] == '(' or str_chk[idx] == '{':
#             stk.append(str_chk[idx])
#         elif str_chk[idx] == ')':
#             if stk == []:
#                 result = 0
#                 break
#             else:
#                 chk = stk.pop()
#                 if chk == '(':
#                 else:
#                     result = 0
#                     break
#
#         elif str_chk[idx] == '}':
#             if stk == []:
#                 result = 0
#                 break
#             else:
#                 chk = stk.pop()
#                 if chk == '{':
#                 else:
#                     result = 0
#                     break
#     if stk:
#         result = 0
#
#     print('#{} {}'.format(tc+1, result))

#########################################################
# 반복문자 지우기

# test_case = int(input())
#
# for tc in range(test_case):
#     str_chk = input()
#     stk = []
#     cnt = 0
#     for idx in range(len(str_chk)):
#         if stk:
#             if stk[-1] == str_chk[idx]:
#                 stk.pop()
#                 cnt -= 1
#                 continue
#             else:
#                 stk.append(str_chk[idx])
#                 cnt += 1
#         else:
#             stk.append(str_chk[idx])
#             cnt += 1
#     print('#{} {}'.format(tc+1, cnt))

#########################################################
# 인접행렬

# adj = [
# #     0 1 2 3 4  to/from
#      [0,0,0,0,0], # 0
#      [0,0,0,0,0], # 1
#      [0,0,0,0,0], # 2
#      [0,0,0,0,0], # 3
#      [0,0,0,0,0], # 4
# ]
#
# # edge 개수만큼 1이 저장됨
# # [from][to] 로 저장한다
# adj[0][1] = 1
# adj[1][2] = 1
# adj[1][3] = 1
# adj[2][0] = 1
# adj[2][4] = 1
# adj[3][4] = 1
# print(adj)

#########################################################
# dfs

# adj = [
#     [0 for _ in range(8)] for _ in range(8)
# ]
#
# adj[0][1] = 1
# adj[0][2] = 1
# adj[1][3] = 1
# adj[1][4] = 1
# adj[2][5] = 1
# adj[5][6] = 1
# adj[5][7] = 1
# de = -1
#
# parents_node = int(input())
# for r in range(8):
#    for c in range(8):
#        if r == parents_node and adj[r][c] != 0:
#            print(c, end=' ')

#########################################################
# dfs - 교수님 풀이

# adj = [
#     [0 for _ in range(8)] for _ in range(8)
# ]
#
# adj[0][1] = 1
# adj[0][2] = 1
# adj[1][3] = 1
# adj[1][4] = 1
# adj[2][5] = 1
# adj[5][6] = 1
# adj[5][7] = 1
#
#
# now = int(input())
#
# #[now][next] now->next 화살표가 있다
# for next in range(0,7+1):
#     if adj[now][next] == 1:
#         print(next, end = ' ')

#########################################################
# 트리형태 DFS 트레이스 - 교수님 풀이

# adj = [
#     [0 for _ in range(8)] for _ in range(8)
# ]
#
# adj[0][1] = 1
# adj[0][2] = 1
# adj[1][3] = 1
# adj[1][4] = 1
# adj[2][5] = 1
# adj[5][6] = 1
# adj[5][7] = 1
#
#
# def dfs(now):
#     # 자식노드 찾기
#     for next in range(8):
#         if adj[now][next] == 1:  # now->next
#             dfs(next)
#
#     return
#
#
# dfs(0)

#########################################################
# 트리형태 DFS 트레이스 (중복되는 경우 방지하기 위한 코드)

# adj = [
#     [0, 1, 1, 1],
#     [1, 0, 0, 1],
#     [0, 1, 0, 1],
#     [0, 0, 0, 0],
# ]
#
#
# def dfs(now):
#     for next in range(4):
#         if adj[now][next] == 1 and visited[next] == 0:  # 연결? 방문안함?
#             visited[next] = 1  # 다시 재귀호출 방지
#             dfs(next)
#     return
#
# visited = [0, 0, 0, 0]
# visited[0] = 1  # 시작노드 0번 방문체크 (이후의 재귀호출에서 다시 재귀호출 방지가능)
# dfs(0)
# de = -1


#########################################################
# 그래프 경로
# def path_chk(node):
#     for idx in range(V+1):
#         if adj[node][idx] == 1 and visited[idx] == 0:
#             visited[idx] = 1
#             path_chk(idx)
#     return
#
# test_case = int(input())
#
# for tc in range(test_case):
#     V, E = map(int, input().split())
#     adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
#     for _ in range(E):
#         e1, e2 = map(int, input().split())
#         adj[e1][e2] = 1
#     S, G = map(int, input().split())
#     visited = [0] * (V+1)
#     visited[S] = 1
#     path_chk(S)
#     print('#{} {}'.format(tc+1, visited[G]))


#########################################################
# 비밀번호

# for tc in range(1, 11):
#     n, str_n = input().split()
#     n = int(n)
#     stk = []
#     cnt = 0
#     for idx in range(n):
#         if stk:
#             if stk[-1] == str_n[idx]:
#                 stk.pop()
#                 cnt -= 1
#             else:
#                 stk.append(str_n[idx])
#                 cnt += 1
#         else:
#             stk.append(str_n[idx])
#     result = ''.join(stk)
#     print('#{} {}'.format(tc, result))

#########################################################
# 길찾기

# def path_chk(node):
#     for i in range(100):
#         if adj[node][i] == 1 and visited[i] == 0:
#             visited[i] = 1
#             path_chk(i)
#     return
#
#
# for tc in range(1, 11):
#     t, n = list(map(int, input().split()))
#     lst_n = list(map(int, input().split()))
#     adj = [[ 0 for _ in range(100)] for _ in range(100)]
#     for idx in range(0, n*2, 2):
#         adj[lst_n[idx]][lst_n[idx+1]] = 1
#
#     visited = [0] * 100
#     visited[0] = 1
#     path_chk(0)
#     print('#{} {}'.format(t, visited[99]))
