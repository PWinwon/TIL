def list_sum(in_list):
    result = 0
    for i in in_list:
        result += i
    return result

sm = list_sum([1, 2, 3, 4, 5])
print(sm)