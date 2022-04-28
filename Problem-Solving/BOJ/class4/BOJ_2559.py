N, K = map(int, input().split())

lst = list(map(int, input().split()))

result = sum(lst[:K])
temp = result
for i in range(K, N):
    temp -= lst[i-K]
    temp += lst[i]
    if result < temp:
        result = temp

print(result)