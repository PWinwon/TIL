T = int(input())

for i in range(T):
    list_n = list(map(int, input().split()))
    sum_list = sum(list_n)-max(list_n)-min(list_n)
    result = round(sum_list / 8 , 0)

    print(f'#{i+1} {int(result)}')