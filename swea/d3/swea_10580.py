T = int(input())


for t in range(T):
    N = int(input())
    list_n = []
    result = 0
    for n in range(N):
        list_ab = list(map(int,input().split()))
        for line in list_n:
            if line[0] < list_ab[0] and line[1] > list_ab[1]:
                result += 1
            elif line[0] > list_ab[0] and line[1] < list_ab[1]:
                result += 1
        list_n.append(list_ab)

    print(f'#{t+1} {result}')
