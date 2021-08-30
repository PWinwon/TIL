N = int(input())
lst_n = list(map(int, input().split()))
my_sub = [0] * N
my_sub[0] = lst_n[0]
max_val = my_sub[0]
chk = 0
for i in range(1, N):
    my_sub[i] += my_sub[i-1] + lst_n[i]
for i in range(N):
    my_sub[i] += chk
    if my_sub[i] < 0:
        chk -= my_sub[i]
    if max_val < my_sub[i]:
        max_val = my_sub[i]
print(max_val)