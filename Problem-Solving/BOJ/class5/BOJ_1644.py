import sys

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input().strip())

primes = [0 for _ in range(N+1)]

primes[0], primes[1] = 1, 1

for i in range(2, int((N+1)**0.5)+1):
    idx = i + i
    while idx <= N:
        primes[idx] = 1
        idx += i

prime_nums = []
for i in range(2, N+1):
    if primes[i] == 0:
        prime_nums.append(i)

lIdx = 0
rIdx = 0
total = 0

if primes[N] == 0:
    result = 1
else:
    result = 0

while lIdx <= rIdx < len(prime_nums):
    if total < N:
        total += prime_nums[rIdx]
        rIdx += 1
    elif total > N:
        total -= prime_nums[lIdx]
        lIdx += 1
    elif total == N:
        result += 1
        total += prime_nums[rIdx]
        rIdx += 1

print(result)