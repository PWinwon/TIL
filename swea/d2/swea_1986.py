T = int(input())

for i in range(T):
    N = int(input())
    result = 0
    for num in range(1,N+1):
        if num % 2 == 0:
            num *= (-1)
        result += num
    
    print(f'#{i+1} {result}')
