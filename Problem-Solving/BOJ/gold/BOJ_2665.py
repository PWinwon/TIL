import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input().strip())

MAP = [list(input().strip()) for _ in range(N)]
used = [[INF for _ in range(N)] for _ in range(N)]


h = []
#       cnt, y, x
heappush(h, [0, 0, 0])
used[0][0] = 0

while h:
    cnt, y, x = heappop(h)
    if y == N-1 and x == N-1:
        print(cnt)
        break
    for i in range(4):
        yr, xr = y+dr[i], x+dc[i]
        if yr < 0 or yr >= N or xr < 0 or xr >= N:
            continue
        if MAP[yr][xr] == '0' and used[yr][xr] > cnt + 1:
            heappush(h, [cnt+1, yr, xr])
            used[yr][xr] = cnt+1
            continue
        if MAP[yr][xr] == '1' and used[yr][xr] > cnt:
            heappush(h, [cnt, yr, xr])
            used[yr][xr] = cnt
            continue


