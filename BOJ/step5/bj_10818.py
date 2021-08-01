import sys

n = int(input())
list_a = list(map(int,sys.stdin.readline().split()))

l_max = list_a[0]
l_min = list_a[0]

for i in range(0,n):
    if(l_max <= list_a[i]):
        l_max = list_a[i]
    if(l_min >= list_a[i]):
        l_min = list_a[i]

print(f'{l_min} {l_max}')