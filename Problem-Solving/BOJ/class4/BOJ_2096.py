import sys

N = int(input())

max_lst = [[0 for _ in range(3)] for _ in range(2)]
min_lst = [[0 for _ in range(3)] for _ in range(2)]

for n in range(N):
    temp = list(map(int, sys.stdin.readline().split()))

    max_lst[1][0] = max(max_lst[0][0], max_lst[0][1]) + temp[0]
    max_lst[1][1] = max(max_lst[0][0], max_lst[0][1], max_lst[0][2]) + temp[1]
    max_lst[1][2] = max(max_lst[0][1], max_lst[0][2]) + temp[2]

    min_lst[1][0] = min(min_lst[0][0], min_lst[0][1]) + temp[0]
    min_lst[1][1] = min(min_lst[0][0], min_lst[0][1], min_lst[0][2]) + temp[1]
    min_lst[1][2] = min(min_lst[0][1], min_lst[0][2]) + temp[2]

    max_lst[0][0], max_lst[0][1], max_lst[0][2] = max_lst[1][0], max_lst[1][1], max_lst[1][2]
    min_lst[0][0], min_lst[0][1], min_lst[0][2] = min_lst[1][0], min_lst[1][1], min_lst[1][2]

print(max(max_lst[1]), min(min_lst[1]))