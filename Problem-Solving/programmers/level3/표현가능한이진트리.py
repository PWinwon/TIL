flag = False


def my_func(left, right, before_num, l):
    global flag
    if flag:
        return
    mid = (left + right) // 2
    if before_num == 0 and l[mid] == 1:
        flag = True
        return
    if left == right:
        return
    my_func(left, mid-1, l[mid], l)
    my_func(mid+1, right, l[mid], l)
    return


def solution(numbers):
    global flag
    answer = []

    for number in numbers:
        idx = 1
        h = 2
        flag = False
        while number >= (1 << idx):
            idx += h
            h *= 2
        lst = [0 for _ in range(idx)]
        i = 0
        while i < idx:
            if number & (1 << i):
                lst[i] = 1
            i += 1
        # print(idx)
        my_func(0, idx-1, 1, lst)
        if flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer