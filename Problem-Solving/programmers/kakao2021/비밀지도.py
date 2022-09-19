def solution(n, arr1, arr2):
    answer = []
    num_lst = []
    idx = 0
    while idx < n:
        a, b = arr1[idx], arr2[idx]
        num_lst.append(a|b)
        idx += 1

    for num in num_lst:
        temp = ''
        idx = n-1
        while idx >= 0:
            if num & 2**idx:
                temp += '#'
            else:
                temp += ' '
            idx -= 1
        answer.append(temp)

    return answer