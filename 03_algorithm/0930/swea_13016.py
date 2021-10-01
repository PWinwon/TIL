LARGER_TEN = ['A', 'B', 'C', 'D', 'E', 'F']


def hex_to_bin(s):
    temp = ''
    if s in LARGER_TEN:
        tar = ord(s) - ord('A') + 10
    else:
        tar = ord(s) - ord('0')
    for i in range(4):
        if tar & (1 << i):
            temp = '1' + temp
        else:
            temp = '0' + temp
    return temp


T = int(input())

for tc in range(T):
    N, num = input().split()
    N = int(N)
    result = ''
    for n in range(N):
        result += hex_to_bin(num[n])
    print('#{} {}'.format(tc+1, result))
