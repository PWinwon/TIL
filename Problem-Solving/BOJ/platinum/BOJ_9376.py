from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    used = [[-1 for _ in range(C+2)] for _ in range(R+2)]
    used[r][c] = 0
    que = deque()
    que.append([r, c])

    while que:
        row, col = que.popleft()
        for i in range(4):
            r_idx = row + dr[i]
            c_idx = col + dc[i]
            if r_idx < 0 or r_idx >= R+2 or c_idx < 0 or c_idx >= C+2:
                continue
            if used[r_idx][c_idx] >= 0:
                continue
            if MAP[r_idx][c_idx] == '*':
                continue
            if MAP[r_idx][c_idx] == '.':
                used[r_idx][c_idx] = used[row][col]
                que.appendleft([r_idx, c_idx])
            elif MAP[r_idx][c_idx] == '#':
                used[r_idx][c_idx] = used[row][col] + 1
                que.append([r_idx, c_idx])
    return used



T = int(input())

# 지도 정보
# . : 빈공간
# * : 벽 통과x
# # : 문 통과o cnt+1
# $ : 죄수위치

for tc in range(T):
    R, C = map(int, input().split())
    MAP = []
    MAP.append(['.']*(C+2))
    for r in range(R):
        MAP.append(['.']+list(input())+['.'])
    MAP.append(['.']*(C+2))

    person = []

    for r in range(R+2):
        for c in range(C+2):
            if MAP[r][c] == '$':
                person.append([r, c])
                MAP[r][c] = '.'


    ans1 = bfs(person[0][0], person[0][1])
    ans2 = bfs(person[1][0], person[1][1])
    ans3 = bfs(0, 0)

    result = 100*100+1

    for r in range(R+2):
        for c in range(C+2):
            if MAP[r][c] == '*' or (ans1[r][c] < 0 or ans2[r][c] < 0 or ans3[r][c] < 0):
                continue
            temp = ans1[r][c] + ans2[r][c] + ans3[r][c]
            if MAP[r][c] == '#':
                temp -= 2
            if result > temp:
                result = temp
    print(result)