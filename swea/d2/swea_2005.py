T = int(input())

for i in range(T):
    N = int(input())
    print(f'#{i+1}')
    for n in range(1,N+1):
        # 출력하기 전 모든 삼각형의 줄(가로)의 요소는 1로 초기화시키고
        # 파스칼 삼각형의 조건에 따라 바로 전의 줄 요소에 슬라이싱을 통해 각 요소에 값을 조건에 맞추어 바꾸어줌
        n_list = [1] * n
        if n > 2:
            for idx in range(1,n-1):
                n_list[idx] = sum(before_l[idx-1:idx+1])
            for x in n_list:
                before_l = n_list
                print(x, end = ' ')
            print('')
        else:
            for x in n_list:
                before_l = n_list
                print(x, end = ' ')
            print('')
    

