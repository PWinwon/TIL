test_case = int(input())

for tc in range(test_case):
    s = input()
    result = 0
    for i in range(1, 11):
        pattern = s[:i]
        sample = (pattern * (30//1 + 1))[:30]
        if s == sample:
            result = i
            break
    print('#{} {}'.format(tc+1, result))
