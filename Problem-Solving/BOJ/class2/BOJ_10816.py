N = int(input())
lst_n = list(map(int, input().split()))

result = [0] * 20000002

for n in range(N):
    result[lst_n[n]+10000000] += 1

M = int(input())
lst_m = list(map(int, input().split()))

for m in range(M):
    if m == M-1:
        print(result[lst_m[m]+10000000])
    else:
        print(result[lst_m[m]+10000000], end=" ")