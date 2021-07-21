def dict_list_sum(dl):
    cnt = 0
    total = 0
    for i in dl:
        cnt += 1
    for j in range(cnt):
        total += dl[j]['age']
    return total

result = dict_list_sum([{'name' : 'kim', 'age': 12}, {'name' : 'lee', 'age': 4}])
print(result)
