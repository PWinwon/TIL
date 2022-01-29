# def my_func(k, n):
#     if n == 1:
#         return 1
#     elif k == 0:
#         return n
#     return my_func(k-1, n) + my_func(k, n-1)
#
# T = int(input())
#
# for tc in range(T):
#     K = int(input())
#     N = int(input())
#     result = my_func(K, N)
#     print(result)


T = int(input())

for tc in range(T):
    K = int(input())
    N = int(input())

    MAP = [i for i in range(1, N+1)]

    for k in range(K):
        for n in range(1, N):
            MAP[n] += MAP[n-1]
    print(MAP[-1])