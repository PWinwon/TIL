T = int(input())

for tc in range(T):
    N = int(input())
    trees = list(map(int, input().split()))
    temp = [0] * N
    trees.sort()
    idx = N // 2
    cnt = 0
    while cnt < N:
        temp[idx] = trees[cnt]
        if cnt % 2:
            idx += cnt + 1
        else:
            idx -= cnt + 1
        cnt += 1
    res = -1
    for i in range(N):
        t = abs(temp[i] - temp[(i+1)%N])
        if res < t:
            res = t
    print(res)