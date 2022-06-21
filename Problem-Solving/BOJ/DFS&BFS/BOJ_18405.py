import sys
import heapq

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, K = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

S, R, C = map(int, input().split())

s = 0

n_h = []

for r in range(N):
    for c in range(N):
        if MAP[r][c]:
            heapq.heappush(n_h, [MAP[r][c], r, c])


while S > s:
    h = n_h
    n_h = []
    while h:
        cnt, y, x = heapq.heappop(h)
        for i in range(4):
            yr, xr = y+dr[i], x+dc[i]
            if yr < 0 or yr >= N or xr < 0 or xr >= N:
                continue
            if MAP[yr][xr]:
                continue
            MAP[yr][xr] = cnt
            heapq.heappush(n_h, [cnt, yr, xr])
    s += 1

print(MAP[R-1][C-1])