import sys

N, M = map(int, input().split())

pm = dict()
pm_lst = [0]

for n in range(1, N+1):
    po = sys.stdin.readline().strip()
    pm[po] = n
    pm_lst.append(po)

for m in range(M):
    po = sys.stdin.readline().strip()
    if po.isalpha():
        print(pm[po])
    else:
        print(pm_lst[int(po)])