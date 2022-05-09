import sys
input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split()))
M = int(input().strip())

lst_sum = [0] * (N+1)

for n in range(N):
    lst_sum[n+1] = lst_sum[n] + lst[n]


for m in range(M):
    a, b = map(int, input().split())
    print(lst_sum[b] - lst_sum[a-1])