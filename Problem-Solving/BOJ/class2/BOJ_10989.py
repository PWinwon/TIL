import sys

N = int(input())

lst = [0] * 10001

for n in range(N):
    num = int(sys.stdin.readline())
    lst[num] += 1


for n in range(10001):
    if lst[n]:
        for i in range(lst[n]):
            print(n)