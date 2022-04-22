def my_fact(n):
    ret = 1
    for i in range(n):
        ret *= (i+1)
    return ret

N, M = map(int, input().split())

if M > (N//2):
    M = N - M

print(my_fact(N)//(my_fact(M)*my_fact(N-M)))