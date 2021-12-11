K, N = map(int, input().split())

k_lst = []
max_len = 0
for k in range(K):
    temp = int(input())
    if max_len < temp:
        max_len = temp
    k_lst.append(temp)
left = 1
right = max_len
result = 0
while True:
    mid = (left + right) // 2
    total = 0
    for i in range(K):
        total += k_lst[i] // mid

    if total >= N:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

    if left > right:
        break

print(right)