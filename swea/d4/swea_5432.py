test_case = int(input())

for tc in range(test_case):
    slice_str = input()
    cnt = 0
    total = 0
    for slc in range(len(slice_str)):
        if slice_str[slc] == '(' and slice_str[slc+1] == ')':
            total += cnt
        elif slice_str[slc] == '(':
            cnt += 1
            total += 1
        elif slice_str[slc] == ')' and slice_str[slc-1] != '(':
            cnt -= 1
    print('#{} {}'.format(tc+1, total))
