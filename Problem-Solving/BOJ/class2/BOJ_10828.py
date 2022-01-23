import sys

N = int(input())

stck = []

s_size = 0

for n in range(N):
    temp = sys.stdin.readline().split()
    if temp[0] == 'push':
        stck.append(temp[1])
    elif temp[0] == 'pop':
        if stck:
            print(stck.pop())
        else:
            print(-1)
    elif temp[0] == 'size':
        print(len(stck))
    elif temp[0] == 'top':
        if stck:
            print(stck[-1])
        else:
            print(-1)
    else:
        if stck:
            print(0)
        else:
            print(1)