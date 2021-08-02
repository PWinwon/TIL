def all_list_sum(list_2d):
    cnt = 0
    total = 0
    for i in list_2d:
        for j in i:
            total += j
    return total

result = all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
print(result)