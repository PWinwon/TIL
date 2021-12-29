def my_fun(num):
    ret = 0
    while num:
        n = num % 10
        num = num // 10
        ret += n

    return ret


N = int(input())

for r in range(1, 1000000):
    temp = my_fun(r)
    if r + temp == N:
        print(r)
        break
else:
    print(0)