def my_func(level, total):
    global result
    if level == N:
        if result > total:
            result = total
            return
    if result < total:
        return
    for i in range(N):
        if used[i] != 0:
            continue
        used[i] = 1
        my_func(level+1, total+lst[level][i])
        used[i] = 0
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    result = 99 * N
    my_func(0, 0)
    print('#{} {}'.format(tc, result))

##########################################################################
# 교수님 풀이

# def func(level , sum):
#     global min_sum
#     if min_sum < sum : return
#     if level == N :
#         min_sum = min(min_sum, sum)
#         return
#     for i in range(N):
#         if used[i] == 1 : continue # 공장이 이전에 사용됨
#         used[i] = 1 # 이후의 재귀호출 선택 금지
#         func(level + 1, sum + MAP[level][i])
#         used[i] = 0 # 원상복구
#
#     return
#
# T = int(input())
#
# for tc in range(1, T + 1) :
#     N = int(input())
#     MAP = [
#         list(map(int ,input().split())) for _ in range(N)
#     ]
#     used = [0] * N
#     min_sum = int(21e8)
#     func(0, 0)
#     print("#{} {}".format(tc, min_sum))