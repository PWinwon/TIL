def my_chk(row, col):
    temp = (row + col) % 2
    if temp and MAP[row][col] == 'B':
        return True
    elif temp==0 and MAP[row][col] == 'W':
        return True
    return False


R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]

result = R * C
for rs in range(0, R-7):
    for cs in range(0, C-7):
        cnt = 0
        for r in range(rs, rs+8):
            for c in range(cs, cs+8):
                if my_chk(r, c):
                    cnt += 1
        if cnt > 32:
            cnt = 64 - cnt
        if result > cnt:
            result = cnt

print(result)