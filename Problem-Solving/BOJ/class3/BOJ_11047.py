import sys

N, K = map(int, input().split())

coin_lst = []
result = 0

for n in range(N):
    coin = int(sys.stdin.readline().strip())
    if coin <= K:
        coin_lst.append(coin)


for n in range(len(coin_lst)-1, -1, -1):
    c = coin_lst[n]
    result += (K // c)
    K = K%c

print(result)