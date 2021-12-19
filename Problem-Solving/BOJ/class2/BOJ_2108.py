N = int(input())

sum = 0
max_val = -4001
min_val = 4001
lst = []

for n in range(N):
    num = int(input())
    sum += num
    if max_val < num:
        max_val = num
    if min_val > num:
        min_val = num
    lst.append(num)

lst_range = max_val - min_val


lst.sort()
lst_cnt = [0] * (lst_range+1)

for i in range(N):
    lst_cnt[lst[i]-min_val] += 1

most_num = -4001
most_cnt = -1
most_result = -4001
for j in range(lst_range, -1, -1):
    if lst_cnt[j] > most_cnt:
        most_num = j+min_val
        most_cnt = lst_cnt[j]
        most_result = j+min_val

    elif lst_cnt[j] == most_cnt:
        most_result = most_num
        most_num = j+min_val


print(int(round(sum/N, 0)))
print(lst[N//2])
print(most_result)
print(lst_range)
