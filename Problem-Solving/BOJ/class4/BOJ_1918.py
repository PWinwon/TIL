import sys

input = sys.stdin.readline

operation_dict = {
    '+': 1, '-': 1, '*': 2, '/': 2, '(': 0
}

temp = input().strip()

stck = []
result = []

for t in temp:
    if 'A' <= t <= 'Z':
        result.append(t)
    elif t == '(':
        stck.append(t)
    elif t == ')':
        while stck and stck[-1] != '(':
            result.append(stck.pop())
        stck.pop()
    else:
        while stck and operation_dict[t] <= operation_dict[stck[-1]]:
            result.append(stck.pop())
        stck.append(t)

while stck:
    result.append(stck.pop())

print(''.join(result))