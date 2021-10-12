def hex_to_int(n):
    ret = 0
    for idx in range(len(n)):
        temp = ord(n[idx])
        if 0 <= (temp - ord('0')) <= 9:
            ret += (temp-ord('0')) * 16**(len(n)-idx-1)
        else:
            ret += (10 + temp-ord('A')) * 16**(len(n)-idx-1)
    return ret


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = input()
    nums += nums[:N//4-1]
    result = set()
    for j in range(N//4):
        for i in range(j, N+N//4-1, N//4):
            res = hex_to_int(nums[i:i+N//4])
            result.add(res)
    result = list(result)
    result.sort(reverse=True)
    print('#{} {}'.format(tc, result[K-1]))