T = int(input())

for i in range(T):
    N = int(input())
    result = []
    cnt = 1
    res = 0
    while len(result) < 10:
        copy_N = N * cnt
        while copy_N > 0:
            if (copy_N % 10) not in result:
                result.append(copy_N % 10)
            copy_N = copy_N // 10
            if len(result) == 10:
                res = N * cnt
                break
        cnt += 1
    print(f'#{i+1} {res}')
