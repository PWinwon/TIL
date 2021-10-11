def my_score():
    score_a = 0
    score_b = 0
    for r in range(N):
        for c in range(r+1, N):
            if used[r] and used[c]:
                score_a += sng[r][c] + sng[c][r]
            elif used[r] == 0 and used[c] == 0:
                score_b += sng[r][c] + sng[c][r]
    return score_a, score_b


def my_recipe(level, c):
    global result
    if c == N//2:
        a, b = my_score()
        if result > abs(a-b):
            result = abs(a-b)
        return
    if level == N:
        return
    used[level] = 1
    my_recipe(level+1, c+1)
    used[level] = 0
    my_recipe(level+1, c)
    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    sng = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    result = 200000
    my_recipe(0, 0)
    print('#{} {}'.format(tc, result))