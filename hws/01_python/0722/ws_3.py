def get_strog_word(a, b):
    sum_a = 0
    sum_b = 0
    for idx in a:
        sum_a += ord(idx)
    for idx in b:
        sum_b += ord(idx)
    if sum_a >= sum_b:
        return a
    else:
        return b

result1 = get_strog_word('z','a')
result2 = get_strog_word('tom','john')

print(result1)
print(result2)