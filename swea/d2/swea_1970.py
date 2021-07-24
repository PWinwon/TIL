# 돈 종류를 담은 리스트
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for i in range(T):
    N = int(input())
    # 결과 값을 담을 리스트
    result = [0] * 8
    for money in range(8):
        # while 반복문을 이용해 같은 돈을 계속 빼는 
        # 연산을 하고 값이 음수가 되면 break
        while True:
            if N - money_list[money] < 0:
                break
            else:
                N -= money_list[money]
                result[money] += 1
    print(f'#{i+1}')
    for j in range(8):
        print(result[j], end = ' ')
    print('')

