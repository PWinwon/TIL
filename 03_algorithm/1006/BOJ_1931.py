import sys

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst.sort(key=lambda x:(x[1], x[0]) )
cnt = 0
time = 0
for i in range(N):
    if lst[i][0] >= time:
        cnt += 1
        time = lst[i][1]
print(cnt)