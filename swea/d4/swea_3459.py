result_lst = []

test_case = int(input())

for tc in range(test_case):
    num = int(input())
    if num == 1:
        result = 1
    num -= 1
    who_win = 8
    while num > 0:
        if num > who_win:
            num -= who_win
            who_win *= 4
        elif (num-1) // (who_win // 2) == 0:
            result = 0
            break
        elif (num-1) // (who_win // 2) == 1:
            result = 1
            break
    if result == 0:
        result_lst.append('#{} Alice'.format(tc+1))
    else:
        result_lst.append('#{} Bob'.format(tc+1))
    
for t in range(test_case):
    print(result_lst[t])