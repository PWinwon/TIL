test_case = int(input())

for tc in range(test_case):
    string_p = input().strip()
    string_q = input().strip()
    result = 'Y'
    if (string_p + 'a') == string_q:
        result = 'N'

    print('#{} {}'.format(tc+1, result))