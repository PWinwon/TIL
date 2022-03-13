def my_func(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return my_func(num-1) + my_func(num-2) + my_func(num-3)


T = int(input())

for tc in range(T):
    N = int(input())
    ret = my_func(N)
    print(ret)