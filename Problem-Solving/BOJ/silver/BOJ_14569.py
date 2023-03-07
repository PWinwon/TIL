import sys

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input().strip())

classes = []
for n in range(N):
    temp = 0
    lst = list(map(int, input().split()))
    for i in range(lst[0]):
        temp |= 1 << lst[i+1]
    classes.append(temp)

# print(classes)

M = int(input().strip())
for m in range(M):
    s = list(map(int, input().split()))
    temp = 0
    for i in range(s[0]):
        temp = temp | 1 << s[i+1]
    ret = 0
    for cl in classes:
        if cl & temp == cl:
            ret += 1
    print(ret)