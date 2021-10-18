# BOB = 0 , Alice = 1

# lst_win = [0] * (10**18)
# idx = 0
# who = 1
# fourth = 4
# cnt = 0
# while idx < 10**18 - 1:
#     lst_win[idx+1] = who
#     idx += 1
#     cnt += 1
#     if cnt == fourth:
#         idx += fourth
#         fourth *= 4
#         cnt = 0
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
