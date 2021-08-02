cnt = 0

numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
for number in numbers:
    cnt += 1

j = 0

idx_list = [0] * cnt
result_list = [0] * cnt

for number in numbers:
    idx = 0
    for i in range(cnt):
        if number > numbers[i]:
            idx += 1
    idx_list[j] = idx
    j += 1

for idx_nx in idx_list:
    ck_nx = 0
    for ii in range(cnt):
        if idx_nx == idx_list[ii]:
            if ck_nx :
                idx_list[ii] += 1
            else:
                ck_nx += 1

idx2 = 0
for k in idx_list:
    result_list[k] = numbers[idx2]
    idx2 += 1

print(result_list[cnt//2])