test_case = int(input())

# 10보다 클때는 -1, 나머지는 곱을 처리
# 출력
for tc in range(test_case):
    a, b = map(int, input().split())

    if a >= 10 or b >= 10:
        result = -1
    else:
        result = a * b
    
    print('#{} {}'.format(tc+1, result))