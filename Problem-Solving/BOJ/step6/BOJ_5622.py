import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

temp = input().strip()

result = 0

for t in temp:
    result += 3
    chk = (ord(t) - ord('A'))
    if chk >= 18:
        chk -= 1
    if chk == 24:
        chk -= 1
    result += chk//3
print(result)
