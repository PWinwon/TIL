test_case = int(input())

chk = ['1', '0']

for tc in range(test_case):
    memo = input()
    idx = 0
    result = 0
    for i in range(len(memo)):
        if memo[i] == chk[idx]:
            result += 1
            idx = (idx + 1) % 2
    print('#{} {}'.format(tc+1, result))