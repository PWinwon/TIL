N = int(input())
balls = input()
cnt = [0] * 4
color_front = balls[0]
color_back = balls[-1]
chk = 0
for i in range(N):
    if balls[i] != color_front:
        chk = 1
        cnt[1] += 1
    elif balls[i] == color_front and chk == 1:
        cnt[0] += 1
chk2 = 0
for j in range(N-1, -1, -1):
    if balls[j] != color_back:
        chk2 = 1
        cnt[3] += 1
    elif balls[j] == color_back and chk2 == 1:
        cnt[2] += 1
print(min(cnt))