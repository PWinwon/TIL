test_case = int(input())

for tc in range(test_case):
    n = int(input())
    sentence = ''
    while len(sentence) < n:
        sentence += ''.join(input().split())
    target = 0
    while True:
        chk = 0
        temp = str(target)
        for idx in range(n):
            if temp == sentence[idx:idx+len(temp)]:
                chk = 1
                break
        if chk == 0:
            break
        target += 1
    print('#{} {}'.format(tc+1, target))