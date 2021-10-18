prime_num = []
num_list = [1] * 1000000

# prime_num = []
# num_list = []
# for i in range(1, 1000001):
#     num_list.append(i)
# for idx in range(1, 1000000):
#     num = idx + 1
#     if num == num_list[idx]:
#         prime_num.append(num)
#         for x in range(num, 1000001, num):
#             num_list[x-1] = 0
# 미리 소인수를 100만까지 모조리 구해버림
# 반복을 거치며 수가 1로 남아있을경우 == 소수
# 소수가 생길때마다 그 배수를 다시 0으로 채움
# 합성수는 그 배수를 할 필요가 없음, 이미 소수로 0으로 채운 부분과 겹침
# ex) 2의배수안에 4의 배수가 포함됨
for num in range(2, 1000001):
    sample_num = num - 1
    if num_list[sample_num] == 1:
        prime_num.append(num)
        while sample_num < 1000000:
            num_list[sample_num] = 0
            sample_num += num

# print(len(prime_num))

T = int(input())

for t in range(T):
    D, A, B = map(int,input().split())
    idx = 0
    result = 0
    # 위에서 구한 소수의 리스트의 원소 중 A와 B사이의 값에 대해 D를 포함하는지 확인
    for pn in prime_num:
        if pn >= A:
            if pn <= B:
                while pn:
                    if pn % 10 == D:
                        result+=1
                        break
                    pn = pn // 10
    print(f'#{t+1} {result}')