n = int(input())

cnt = 0
bef_1 = 0
bef_10 = 0
new_n = n

while 1:
    bef_1 = new_n % 10
    bef_10 = new_n // 10
    new_n = ((bef_1 + bef_10) % 10) + (bef_1 * 10)
    cnt = cnt + 1
    if(n == new_n):
        break


print(cnt)