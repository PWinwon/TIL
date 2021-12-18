PRIME = [0, 0] + [1] * 1000

for i in range(2, 1001):
    if PRIME[i] == 1:
        for j in range(i+i, 1001, i):
            PRIME[j] = 0

N = int(input())

lst = list(map(int, input().split()))

result = 0

for l in lst:
    if PRIME[l]:
        result += 1

print(result)