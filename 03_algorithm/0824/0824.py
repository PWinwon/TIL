#######################################################
# 부분집합의 합 연습

# def sub_ox(level, s):
#     if level == 4:
#         ans = ''
#         for i in range(4):
#             if s[i] == 'O':
#                 ans += lst[i]
#         print('{} -> {}'.format(s, ans))
#         return
#     sub_ox(level + 1, s + 'O')
#     sub_ox(level + 1, s + 'X')
#     return
#
#
# lst = ['A', 'B', 'C', 'D']
# sub_ox(0, '')

##########################################################
# 도착 가능한지 여부 출력

# adj = [
#     [0,1,1,1],
#     [1,0,0,1],
#     [0,1,0,1],
#     [0,0,0,0],
# ]
#
# visited = [0,0,0,0]
# def dfs(now) :
#     if now == 3 :
#         print("도착가능!")
#         return
#     for next in range(4):
#         if adj[now][next] == 0 : continue # 연결점 찾기
#         if visited[next] == 1 : continue  # next 가 이미 방문
#         visited[next] = 1
#         dfs(next)
#
#
# visited[0] = 1
# dfs(0)

##########################################################
# 모든 경로 출력

# def path_node(node, path):
#     global cnt
#     if node == 3:
#         print(path)
#         cnt += 1
#         return
#     for i in range(4):
#         if adj[node][i] == 1 and used[i] == 0:
#             used[node] = 1
#             path_node(i, path + str(i))
#             used[node] = 0
#     return
#
#
# adj = [
#     [0,1,1,1],
#     [1,0,0,1],
#     [0,1,0,1],
#     [0,0,0,0],
# ]
#
# cnt = 0
# used = [0] * 4
# path_node(0, '0')
# print('경로의 수 : {}회'.format(cnt))

def dice_cnt(level, s):
    global N
    if level == N:
        print(s)
        return
    for i in range(1, 5):
        dice_cnt(level+1, s+str(i))
    return

# def dice_cnt(level):
#     if level == N:
#         print(result)
#         return
#     for i in range(1, 5):
#         result.append(i)
#         dice_cnt(level+1)
#         result.pop()
#     return

#########################################################
# 교수님 풀이

# path = [0,0,0]
# used = [0,0,0,0,0] # dat로 이용
# def dfs(level):
#     if level == 3 :
#         print(path)
#         return
#     for i in range(1,4+1): # i 가 현재 선택하려는 눈금
#         if used[i] == 1 : continue
#         path[level] = i # 현재 level 에서 i 선택 /// path.append(i)
#         used[i] = 1 # i 눈금을 사용체크
#         dfs(level + 1)
#         used[i] = 0 # 원상복구
#         path[level] = 0 # 원상복구   /// path.pop()
#     return
#
# dfs(0)


def dice_cnt2(level, s):
    if level == N:
        print(s)
        return
    for i in range(1, 5):
        if visited[i-1] == 1:
            continue
        visited[i-1] = 1
        dice_cnt2(level+1, s+str(i))
        visited[i-1] = 0
    return


result = []
N = int(input())
# dice_cnt(0)
visited = [0] * 4
dice_cnt2(0, '')

#########################################################
# 교수님 풀이
# def dfs(level,sum): # sum > min_sum
#     global min_sum
#     if min_sum < sum : return # 가지치기
#     if level == N :
#         # min_sum vs sum
#         if min_sum > sum :
#             min_sum = sum
#         return
#     for x in range(N):
#         if used[x] == 1: continue
#         used[x] = 1 # x 좌표 사용
#         dfs(level+1, sum + MAP[level][x])
#         used[x] = 0 # 원복
#
#
#
# N = int(input())
# MAP = [
#     list(map(int, input().split())) for _ in range(N)
# ]
# used = [0 for _ in range(N)]
# min_sum = int(21e8)
# dfs(0,0)
# print(min_sum)
