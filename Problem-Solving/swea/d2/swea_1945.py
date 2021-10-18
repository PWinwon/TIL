prime_num = [2, 3, 5, 7, 11]

T = int(input())

for i in range(T):
    print(f'#{i+1}', end='')
    N = int(input())
    for p_num in prime_num:
        idx = 0
        while N:
            if N % p_num:
                break
            else:
                N = N // p_num
                idx += 1
        print(f' {idx}', end = '')
    print('')

