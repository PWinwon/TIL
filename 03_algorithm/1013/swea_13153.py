NUM = [2, 3, 5]

def create_ulnum(level, num, idx):
    if level > 30:
        return
    ugl_numbers.append(num)
    for i in range(3):
        if i < idx:
            continue
        create_ulnum(level+1, num * NUM[i], i)
    return

ugl_numbers = []
create_ulnum(1, 1, 0)
ugl_numbers.sort()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = [0] * N
    for j in range(N):
        result[j] = ugl_numbers[lst[j]-1]
    print('#{} {}'.format(tc, ' '.join(map(str, result))))