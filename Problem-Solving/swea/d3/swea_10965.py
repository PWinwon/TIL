# 시간을 최소화 하기위한 범위안의 숫자들의 소인수가 될 수 있는 소수들을 생성
# 범위 내의 소수를 전부 저장하는 것이 아닌 입력받은 값의 소인수범위를 생각하여 생성해주어야함
# ex) 100 이하의 합성수(A)는 10 이하의 소수의 집합(P)로 모두 소인수 분해 가능하다. 단 소수일 경우는 표현 불가능
# 위의 작업은 본 코드에서 적용  
num_lst = [1] * int((10**7)**0.5)
prime_lst = []
for n in range(2, int((10**7)**0.5)):
    if num_lst[n-1] == 1:
        prime_lst.append(n)
        for idx in range(n-1, int((10**7)**0.5), n):
            num_lst[idx] = 0

test_case = int(input())
result_lst = []

# prime_lst에는 범위 안의 합성수의 모든 소인수를 담고 있음
# 즉 합성수일 경우 모두 소인수 분해가능
# prime_lst의 소수들로 나누어 주면서 그 수를 cnt에 누적시켜 cnt가 홀 수 일경우 result에 그값을 곱하여 줌
# 만약 prime_lst를 벗어난 소수의 경우 그 숫자는 무조건 자기 자신을 한 번 더 곱해주어야 제곱수가 될 수 있으므로,
# 그에 대한 처리를 마지막에 하여줌
for tc in range(test_case):
    num = int(input())
    result = 1
    for prime in prime_lst:
        if prime > num:
            break
        cnt = 0
        while num % prime == 0:
            num = num // prime
            cnt += 1
        if cnt % 2 == 1:
            result *= prime
    if num > 1:
        result *= num
    result_lst.append('#{} {}'.format(tc+1, result))
    # 출력에 걸리는 시간이 상당히 길다. 따라서 출력하고 싶은 문자열 형태 그대로 result_lst에 저장
    # 출력은 모든 테스트 케이스의 정답에 대해 result 를 구하여 저장한후 한번에 출력
for re in result_lst:
    print(re)

