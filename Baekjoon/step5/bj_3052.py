#set 안쓰고 알고리즘으로 풀어보기

list_num = [0] * 10
idx = 0

for i in range(10):
    list_num[i] = int(input()) % 42

list_res = set(list_num)

print(len(list_res))
