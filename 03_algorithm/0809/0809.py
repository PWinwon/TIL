
########################################################################################
# 1.

a, b, c = map(int, input().split())

total = a + b + c
my_avg = total // 3
max_val = a
for i in (a, b, c):
    if i > max_val:
        max_val = i

print(my_avg)
print(max_val)

########################################################################################
# 2.

lst = list(map(int, input().split()))
result = []
for l in lst[-1::-1]:
    result.append(l)
print(*result)

########################################################################################
# 3. Gravity

T = int(input())


for t in range(T):
    N = int(input())
    list_n = list(map(int, input().split()))
    max_length = 0
    for idx in range(N):
        check_length = 0
        for idx2 in range(idx+1, N):
            if list_n[idx] > list_n[idx2]:
                check_length += 1
        if check_length > max_length:
            max_length = check_length
    print(f'#{t+1} {max_length}')


########################################################################################
# 4. 

list_test = [3, 2, 1, 3, 2, 5, 7, 9, 7]
list_idx = [0] * 10

for lt in list_test:
    list_idx[lt] += 1

for idx in range(10):
    if list_idx[idx]:
        print(f'{idx} : {list_idx[idx]}개')


########################################################################################
# 5. Baby Gin


T = int(input())

for t in range(T):
    numbers = int(input())
    idx_list = [0] * 10
    for i in range(6):
        idx_list[numbers % 10] += 1
        numbers = numbers // 10
    check_run = 0
    check_tri = 0
    idx = 0
    while idx < 10:
        if idx_list[idx] >= 3:
            check_tri += 1
            idx_list[idx] -= 3
            continue
        if idx <= 7 and idx_list[idx] and idx_list[idx+1] and idx_list[idx+2]:
            check_run += 1
            idx_list[idx] -= 1
            idx_list[idx+1] -= 1
            idx_list[idx+2] -= 1
            continue
        idx += 1
        if check_run + check_tri == 2:
            break
    if check_run + check_tri == 2:
        print(f'#{t+1} Baby Gin')
    else:
        print(f'#{t+1} Lose')


########################################################################################
# 6. View


for t in range(10):
    N = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, N-2):
        sample_result = 255
        for j in range(i-2, i+3):
            if i != j and sample_result >= (building[i] - building[j]):
                sample_result = building[i] - building[j]
        if sample_result > 0:
            result += sample_result
    print(f'#{t+1} {result}')