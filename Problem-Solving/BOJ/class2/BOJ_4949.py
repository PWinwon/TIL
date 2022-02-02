import sys

while True:
    temp = sys.stdin.readline().rstrip()
    if temp == '.':
        break
    stck = []
    result = 'yes'
    for n in temp:
        if n == '(':
            stck.append(n)
        elif n == '[':
            stck.append(n)
        elif n == ')':
            if stck:
                chk = stck.pop()
                if chk != '(':
                    result = 'no'
                    break
            else:
                result = 'no'
                break
        elif n == ']':
            if stck:
                chk = stck.pop()
                if chk != '[':
                    result = 'no'
                    break
            else:
                result = 'no'
                break
    if stck:
        print('no')
    else:
        print(result)