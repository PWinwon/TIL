import sys

T = int(sys.stdin.readline())

for t in range(T):
    result = sys.stdin.readline()
    score = 0
    total = 0
    for re in result:
        if re == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)
