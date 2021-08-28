# 1: 우, 2: 좌, 3: 하, 4: 상

my_order = [0, 3, 4, 2, 1]

K = int(input())
lst = []
wh_val = [0] * 5
for i in range(6):
    temp = list(map(int, input().split()))
    lst.append(temp)
    wh_val[temp[0]] += temp[1]
idx = 0
a = 0
b = 0
while True:
    if lst[idx%6][0] != my_order[lst[(idx+1)%6][0]]:
       a = lst[idx%6][1]
       b = lst[(idx+1)%6][1]
       break
    idx += 1
print((wh_val[1] * wh_val[3] - a * b) * K)