

N, M = map(int, input().split())

prime_num = [0, 0] + [1] * (M-1)

for i in range(2, M+1):
    num = i + i
    if prime_num[i] == 1:
        while num <= M:
            prime_num[num] = 0
            num += i
for j in range(N, M+1):
    if prime_num[j]:
        print(j)

