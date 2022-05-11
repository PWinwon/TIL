import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

a = 0
b = 0

result = []

while a < N or b < M:
    if a >= N:
        result.append(lst_b[b])
        b += 1
    elif b >= M:
        result.append(lst_a[a])
        a += 1
    elif lst_a[a] < lst_b[b]:
        result.append(lst_a[a])
        a += 1
    else:
        result.append(lst_b[b])
        b += 1

print(' '.join(map(str, result)))