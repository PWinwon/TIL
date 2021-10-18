from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

paper = [[0 for _ in range(100)] for _ in range(100)]
used = [[0 for _ in range(100)] for _ in range(100)]
result = 0
N = int(input())
que = deque()
for i in range(N):
    x, y = map(int, input().split())
    que.append([y, x])
    used[y][x] = 1
    for r in range(y, y+10):
        for c in range(x, x+10):
            paper[r][c] = 1

de = -1
while que:
    temp = que.popleft()
    row = temp[0]
    col = temp[1]
    for i in range(4):
        r = row + dr[i]
        c = col + dc[i]
        if r < 0 or r > 99 or c < 0 or c > 99:
            result += 1
            continue
        if used[r][c] == 1:
            continue
        if paper[r][c] == 1:
            que.append([r, c])
            used[r][c] = 1
        if paper[r][c] == 0:
            result += 1

print(result)