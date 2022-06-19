import sys

input = sys.stdin.readline

def my_gcd(aa, bb):
    ret = -1

    if aa > bb:
        s = bb
    else:
        s = aa

    for i in range(1, s+1):
        if (aa % i == 0) and (bb % i == 0):
            ret = i
    return ret


a, b = map(int, input().split(':'))
num = my_gcd(a, b)

print(':'.join(map(str, [a//num, b//num])))