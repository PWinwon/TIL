# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     lst = []
#     for _ in range(N):
#         lst.append(list(map(int, input().split())))
#     lst.sort(key=lambda x:x[1])
#     result = 0
#     time = 0
#     start = 0
#     for l in lst:
#         if l[0] >= time:
#             result += 1
#             time = l[1]
#     print('#{} {}'.format(tc, result))

######################################################################
# 완전탐색 풀이


def my_func(level, c):
    global cnt
    if level == N:
        if cnt < c:
            cnt = c
        return
    temp = lst[level]
    if sum(used[temp[0]:temp[1]+1]) == 0:
        for time in range(temp[0]+1, temp[1]):
            used[time] = 1
        my_func(level+1, c+1)
        for time in range(temp[0]+1, temp[1]):
            used[time] = 0
    my_func(level+1, c)
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * 25
    cnt = 0
    my_func(0, 0)
    print('#{} {}'.format(tc, cnt))