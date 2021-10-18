T = int(input())

for i in range(T):
    N = int(input())
    list_n = list(map(int, input().split()))
    result = []
    # Ai 와 Aj의 곱이 단조수열을 만족하는지 확인하기 위한 반복문 생성
    for ni in range(N):
        for nj in range(ni+1, N):
            # 값을 받아올 a와 단조수열인지 확인을 위한 비교 값 check_a
            # 모든 값에서 만족했는지 확인하기 위한 check_pass
            a = list_n[ni] * list_n[nj]
            check_a = 10
            check_pass = 1
            # 단조수열임을 확인할 a에 대해 10에대한 나머지를 연산하여 check_a 와 반복문을 돌며 계속 비교함
            # 나머지이므로 뒤에 값 부터 비교되므로 점점 작아지는지 확인
            while a:
                if check_a >= a%10:
                    check_a = a % 10
                    a = a // 10
                # 한번이라도 만족하지 않으면 check_pass = 0
                else:
                    check_pass = 0
                    break
            # 모두 단조수열을 만족하면 result에 append로 추가
            if check_pass:
                result.append(list_n[ni] * list_n[nj])
    # 모두 만족하지 않을 경우 즉, result에 값이 없을 때 -1 출력을 위한 조건문
    if not result:
        result.append(-1)
    print(f'#{i+1} {max(result)}')

