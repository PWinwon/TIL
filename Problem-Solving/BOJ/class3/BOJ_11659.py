import sys

input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst_sum = [0]
for n in range(N):
    lst_sum.append(lst_sum[n] + lst[n])


for m in range(M):
    i, j = map(int,input().split())
    print(lst_sum[j] - lst_sum[i-1])