# 1493

test_case = int(input())

for tc in range(test_case):
    N, Pd, Pg = map(int, input().split())
    result = 'Possible'
    if N > 100:
        N = 100

    for i in range(1, N+1):
        if (Pd * i) % 100 == 0:
            result = 'Possible'
            break
    else:
        result = 'Broken'
    
    if Pg == 100 and Pd != 100:
        result = 'Broken'
    
    elif Pg == 0 and Pd != 0:
        result = 'Broken'


    print('#{} {}'.format(tc+1, result))