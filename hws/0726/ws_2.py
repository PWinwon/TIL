def count_blood(cb_list):
    result = {}
    for cb in cb_list:
        result[cb] = cb_list.count(cb)
    return result


c = count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
])

print(c)