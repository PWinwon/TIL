T = int(input())
for tc in range(T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(2)]
    
    for i in range(1, N):
        if i == 1:
            MAP[0][i] += MAP[1][i-1]
            MAP[1][i] += MAP[0][i-1]
        else:
            MAP[0][i] += max(MAP[1][i-1], MAP[1][i-2])
            MAP[1][i] += max(MAP[0][i-1], MAP[0][i-2])
    print(max(MAP[0][N-1], MAP[1][N-1]))