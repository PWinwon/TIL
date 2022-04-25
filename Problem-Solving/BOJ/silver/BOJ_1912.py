N = int(input())
lst = list(map(int, input().split()))

lst_sum = [0] * N
lst_sum[0] = lst[0]

for i in range(1, N):
    lst_sum[i] = max(lst[i], lst[i] + lst_sum[i-1])

print(max(lst_sum))