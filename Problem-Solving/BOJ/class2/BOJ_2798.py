N, M = map(int, input().split())

cards = list(map(int, input().split()))

result = -1

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
           hap = cards[i] + cards[j] + cards[k]
           if hap > result and hap <= M:
               result = hap
print(result)
