money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for i in range(T):
    N = int(input())
    result = [0] * 8
    for money in range(8):
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

