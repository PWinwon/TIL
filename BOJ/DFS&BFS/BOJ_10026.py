from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
lst_n = [list(input()) for _ in range(N)]
rgb_eye = [[0 for _ in range(N)] for _ in range(N)]
used1 = [[0 for _ in range(N)] for _ in range(N)]
used2 = [[0 for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        if lst_n[r][c] == 'B':
            rgb_eye[r][c] = 1
        elif lst_n[r][c] == 'G':
            rgb_eye[r][c] = 2

result1 = 0
result2 = 0
for r in range(N):
    for c in range(N):
        if used1[r][c] == 0:
            result1 += 1
            que = deque()
            que.append([r, c])
            used1[r][c] = 1
            while que:
                temp = que.popleft()
                for i in range(4):
                    rr = temp[0] + dr[i]
                    cc = temp[1] + dc[i]
                    if rr < 0 or rr >= N or cc < 0 or cc >= N:
                        continue
                    if rgb_eye[rr][cc] != rgb_eye[temp[0]][temp[1]]:
                        continue
                    if used1[rr][cc] == 1:
                        continue
                    used1[rr][cc] = 1
                    que.append([rr, cc])
        if used2[r][c] == 0:
            result2 += 1
            que = deque()
            que.append([r, c])
            used2[r][c] = 1
            while que:
                temp = que.popleft()
                for i in range(4):
                    rr = temp[0] + dr[i]
                    cc = temp[1] + dc[i]
                    if rr < 0 or rr >= N or cc < 0 or cc >= N:
                        continue
                    if (rgb_eye[rr][cc] % 2) != (rgb_eye[temp[0]][temp[1]] % 2):
                        continue
                    if used2[rr][cc] == 1:
                        continue
                    used2[rr][cc] = 1
                    que.append([rr, cc])

print(result1, result2)