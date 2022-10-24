import sys
input = sys.stdin.readline

h, m = map(int, input().split())
add_min = int(input().strip())
m = m + add_min
if m >= 60:
    h += m // 60
    m %= 60

if h >= 24:
    h %= 24
print(h, m)