import sys
input = sys.stdin.readline

N = input().strip()

lst = []

for i in N:
    lst.append(i)

lst.sort(reverse=True)
print(''.join(lst))