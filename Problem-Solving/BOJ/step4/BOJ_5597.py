import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

lst = [0 for _ in range(31)]

for i in range(28):
    num = int(input().strip())
    # print(num)
    lst[num] += 1

for j in range(1, 31):
    if lst[j] == 0:
        print(j)