def bfs(now):
    if now > N:
        return
    bfs(now*2)
    print(v_val[now], end='')
    bfs(now*2+1)
    return


for tc in range(1, 11):
    N = int(input())
    lst_n = [list(input().split()) for _ in range(N)]
    v_val = [0] * (N+1)
    for i in range(N):
        v_val[i+1] = lst_n[i][1]
    print('#{} '.format(tc), end='')
    bfs(1)
    print('')