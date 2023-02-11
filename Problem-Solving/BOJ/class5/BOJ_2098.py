import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')


def my_func(n, visited):
    global N, ALL_VISITED
    if visited == ALL_VISITED:
        if MAP[n][0]:
            return MAP[n][0]
        else:
            return INF

    if dp[n][visited] is not None:
        return dp[n][visited]

    min_value = INF
    for x in range(1, N):
        # 방문하지 않았고, 이동가능한 정점 탐색
        if visited & (1 << x) == 0 and MAP[n][x] != 0:
            min_value = min(min_value, my_func(x, visited | (1 << x)) + MAP[n][x])
    dp[n][visited] = min_value
    return min_value


N = int(input().strip())
MAP = [list(map(int, input().split())) for _ in range(N)]
dp = [[None] * (1 << N) for _ in range(N)]
ALL_VISITED = (1 << N) - 1

result = my_func(0, 1)

print(result)