T = int(input())

for i in range(T):
    N = int(input())
    list_n = list(map(int, input().split()))
    
    result = [0] * N
    for ln in list_n:
        idx = 0
        for x in range(N):
            if ln > list_n[x]:
                idx += 1
        while(True):
            if result[idx] == 0:
                result[idx] = ln
                break
            else:
                idx += 1
    print(f'#{i+1}', end = ' ')
    for re in range(N):
        if re == N-1:
            print(result[re])
        else:
            print(result[re], end = ' ')
