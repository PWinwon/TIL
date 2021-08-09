T = int(input())


# 반복문을 통해 값을 누적하면서, 
# 짝수의 경우 -1을 곱한 값을 누적하여
# 문제 조건에 맞는 값을 출력해 낸다.
for i in range(T):
    N = int(input())
    result = 0
    for num in range(1,N+1):
        if num % 2 == 0:
            num *= (-1)
        result += num
    
    print(f'#{i+1} {result}')
