import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def my_func(left, right):
    if left > right:
        return
    else:
        mid = right + 1
        for i in range(left+1, right+1):
            if lst[left] < lst[i]:
                mid = i
                break

        my_func(left+1, mid-1)
        my_func(mid, right)
        print(lst[left])


lst = []

while True:
    try:
        num = int(input().strip())
        lst.append(num)
    except:
        break

my_func(0, len(lst)-1)