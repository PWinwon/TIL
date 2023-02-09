import sys

input = sys.stdin.readline

chars = input().strip()
bomb_str = input().strip()
bomb_len = len(bomb_str)
stck = []

idx = 0
while idx < len(chars):
    stck.append(chars[idx])
    if stck[-1] == bomb_str[-1] and len(stck) >= bomb_len:
        cnt = 0
        for i in range(bomb_len):
            if stck[-i-1] == bomb_str[-i-1]:
                cnt += 1
        if cnt == bomb_len:
            while cnt > 0:
                stck.pop()
                cnt -= 1
    idx += 1

if stck:
    print(''.join(stck))
else:
    print('FRULA')


