T = int(input())

for i in range(T):
    n = int(input())
    list_dalpang = [0] * n
    for j in range(n):
        line = []
        for k in range(n):
            line += [0]
        list_dalpang[j] = line
    max_val = n**2
    x_idx = 0
    y_idx = -1
    pl_mn = 1
    val = 1
    num = n
    while(val <= max_val):
        for y in range(n):
            y_idx += pl_mn
            list_dalpang[x_idx][y_idx] += val
            val += 1
        for x in range(n-1):
            x_idx += pl_mn
            list_dalpang[x_idx][y_idx] = val
            val += 1
        pl_mn *= (-1)
        n -= 1
    print(f'#{i+1}')
    for x in range(num):
        for y in range(num):
            print(list_dalpang[x][y], end = ' ')
        print('')