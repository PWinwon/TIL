R, C, B = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]

block_cnt = 0
for r in range(R):
    for c in range(C):
        block_cnt += MAP[r][c]

# 최대 높이 H
H = min((B + block_cnt) // (R * C), 256)

result_t = 9876543219
result_h = -1

for h in range(H+1):
    t = 0
    for r in range(R):
        for c in range(C):
            if MAP[r][c] > h:
                t += (MAP[r][c] - h) * 2
            elif MAP[r][c] < h:
                t += (h - MAP[r][c])
    if t <= result_t:
        result_t = t
        if h > result_h:
            result_h = h

print(result_t, result_h)