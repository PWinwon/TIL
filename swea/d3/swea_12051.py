test_case = int(input())

# 문제의 조건에서 'Broken'이 나오는 경우에 대해 처리
# 기본값을 'Possible'
# 전체 승률 100과 0에 대해 오늘 승률에 가능성에 대해 생각
# 전체 승률 100이면 오늘 절대 1판도 져서는 안됨
# 전체 승률 0이면 오늘 절대 1판도 이겨서는 안됨
# 표본이 아무리 커도 확률이 정수 --> N의 값이 아무리 커도 100일 때와 같음
# 위의 조건을 고려하여 코드 작성
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