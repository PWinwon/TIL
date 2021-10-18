from collections import deque


def gbox_chk():
    global score
    idx = 5
    while idx >= 2:
        cnt = 0
        for i in range(4):
            if gbox[idx][i] == 1:
                cnt += 1
        if cnt == 4:
            del gbox[idx]
            gbox.appendleft([0 for _ in range(6)])
            score += 1
            continue
        idx -= 1
    while idx >= 0:
        for j in range(4):
            if gbox[idx][j] == 1:
                break
        else:
            break
        gbox.pop()
        gbox.appendleft([0 for _ in range(6)])
    return


def bbox_chk():
    global score
    idx = 5
    while idx >= 2:
        cnt = 0
        for i in range(4):
            if bbox[idx][i] == 1:
                cnt += 1
            else:
                break
        if cnt == 4:
            del bbox[idx]
            bbox.appendleft([0 for _ in range(6)])
            score += 1
            continue
        idx -= 1
    while idx >= 0:
        for j in range(4):
            if bbox[idx][j] == 1:
                break
        else:
            break
        bbox.pop()
        bbox.appendleft([0 for _ in range(6)])
    return


bbox = deque([0 for _ in range(4)] for _ in range(6))
gbox = deque([0 for _ in range(4)] for _ in range(6))


N = int(input())
score = 0
for n in range(N):
    t, x, y = map(int, input().split())
    if t == 1:
        idx = 0
        while idx < 6:
            if gbox[idx][y] == 1:
                break
            else:
                idx += 1
        gbox[idx-1][y] = 1
        idx = 0
        while idx < 6:
            if bbox[idx][x] == 1:
                break
            else:
                idx += 1
        bbox[idx-1][x] = 1
    elif t == 2:
        idx = 1
        while idx < 6:
            if gbox[idx][y] == 1 or gbox[idx][y+1]:
                break
            else:
                idx += 1
        gbox[idx - 1][y] = 1
        gbox[idx - 1][y+1] = 1
        idx = 1
        while idx < 6:
            if bbox[idx][x] == 1:
                break
            else:
                idx += 1
        bbox[idx - 1][x] = 1
        bbox[idx - 2][x] = 1
    else:
        idx = 1
        while idx < 6:
            if gbox[idx][y] == 1:
                break
            else:
                idx += 1
        gbox[idx-1][y] = 1
        gbox[idx-2][y] = 1
        idx = 0
        while idx < 6:
            if bbox[idx][x] == 1 or bbox[idx][x + 1] == 1:
                break
            else:
                idx += 1
        bbox[idx-1][x] = 1
        bbox[idx-1][x+1] = 1
    gbox_chk()
    bbox_chk()
cnt = 0
for r in range(6):
    for c in range(4):
        if gbox[r][c] == 1:
            cnt += 1
        if bbox[r][c] == 1:
            cnt += 1


print(score)
print(cnt)