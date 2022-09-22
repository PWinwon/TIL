def solution(msg):
    answer = []
    my_dict = dict()
    for i in range(1, 27):
        temp = chr(ord('A') + i - 1)
        my_dict[temp] = i
    idx = 0
    my_str = ''
    num = 27
    while idx < len(msg):
        if (my_str + msg[idx]) in my_dict:
            my_str += msg[idx]
            idx += 1
        else:
            answer.append(my_dict[my_str])
            my_dict[my_str + msg[idx]] = num
            num += 1
            my_str = ''
    if my_str:
        answer.append(my_dict[my_str])

    return answer