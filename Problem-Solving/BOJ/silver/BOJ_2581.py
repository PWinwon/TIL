PRIME_NUM = [0, 0] + [1] * 9999

for i in range(10001):
    if PRIME_NUM[i] == 1:
        n = i
        idx = n * n
        while idx < 10001:
            PRIME_NUM[idx] = 0
            idx += n

N = int(input())
M = int(input())
res_sum = 0
min_val = 10001
for num in range(N, M+1):
    if PRIME_NUM[num]:
        res_sum += num
        if min_val > num:
            min_val = num

if res_sum:
    print(res_sum)
    print(min_val)
else:
    print(-1)