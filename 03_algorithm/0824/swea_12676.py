def subsum(level, sum):
    global min_val
    if level == N:
        if min_val > sum:
            min_val = sum
        return
    if sum > min_val:
        return
    for i in range(N):
        if used[i] == 1:
            continue
        used[i] = 1
        subsum(level+1, sum + arr[level][i])
        used[i] = 0
    return


test_case = int(input())

for tc in range(test_case):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_val = 30
    used = [0] * N
    subsum(0, 0)
    print(f'#{tc+1} {min_val}')

##########################################################
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