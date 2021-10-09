CHANGE = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


T = int(input())

for tc in range(1, T+1):
    money = int(input())
    result = [0] * 8
    idx = 0
    while money and idx < 8:
        if CHANGE[idx] > money:
            idx += 1
            continue
        result[idx] = money // CHANGE[idx]
        money = money % CHANGE[idx]
    res = ' '.join(map(str, result))
    print('#{}'.format(tc))
    print(res)