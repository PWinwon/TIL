N, K = map(int, input().split())

result = 1
div = 1

for num in range(N, N-K, -1):
    result *= num

for num in range(1, K+1):
    div *= num

print(result//div)