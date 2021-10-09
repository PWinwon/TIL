lst_2 = ['0', '1']
lst_3 = ['0', '1', '2']


def my_calc(s, num):
    total = 0
    for i in range(len(s)):
        total += int(s[i]) * (num ** (len(s)-i-1))
    return total


def my_func(level):
    if level == l2:
        return
    for i in range(2):
        if lst_2[i] == num_2[level]:
            continue
        temp = num_2[level]
        num_2[level] = lst_2[i]
        ret = my_calc(num_2, 2)
        num_2[level] = temp
        res[ret] = 1
    my_func(level+1)
    return


def my_func3(level):
    global result
    if result:
        return
    if level == l3:
        return
    for i in range(3):
        if lst_3[i] == num_3[level]:
            continue
        temp = num_3[level]
        num_3[level] = lst_3[i]
        ret = my_calc(num_3, 3)
        num_3[level] = temp
        if ret in res.keys():
            result = ret
            return
    my_func3(level+1)
    return


T = int(input())

for tc in range(1, T+1):
    num_2 = list(input())
    num_3 = list(input())
    l2 = len(num_2)
    l3 = len(num_3)
    result = False
    res = {}
    my_func(0)
    my_func3(0)
    t = my_calc('212', 3)
    print('#{} {}'.format(tc, result))