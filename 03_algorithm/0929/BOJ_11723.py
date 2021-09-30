import sys

M = int(input())
pizza = 1 << 21
rem_piz = (1 << 22) - 1

for m in range(M):
    temp = sys.stdin.readline().split()
    oper = temp[0]
    if oper == 'all':
        pizza = (1 << 22) - 1
        continue
    elif oper == 'empty':
        pizza = 1 << 21
        continue
    else:
        num = int(temp[1])-1
    if oper == 'add':
        pizza = (pizza | (1<<num))
    elif oper == 'check':
        if pizza & (1<<num):
            print(1)
        else:
            print(0)
    elif oper == 'remove':
        pizza = (pizza & (rem_piz^(1<<num)))
    elif oper == 'toggle':
        pizza = (pizza ^ (1<<num))