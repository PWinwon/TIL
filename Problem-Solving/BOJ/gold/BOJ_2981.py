import sys
from math import gcd
from math import sqrt

input = sys.stdin.readline

N = int(input().strip())

lst = []
itval = []
ans = []

for n in range(N):
    lst.append(int(input().strip()))

for i in range(1, N):
    itval.append(lst[i] - lst[i-1])

val = itval[0]
for i in range(1, len(itval)):
    val = gcd(val, itval[i])

for i in range(2, int(sqrt(val))+1):
    if val % i == 0:
        ans.append(i)
        ans.append(val//i)

ans.append(val)
ans = list(set(ans))
ans.sort()
print(' '.join(map(str, ans)))