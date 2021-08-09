T = int(input())


for t in range(T):
    N = int(input())
    list_n = []
    result = 0
    # 전봇대의 전선수를 입력받고, 각 전선의 출발점과 도착점을 입력받으면서(전선이 추가되면서)
    # 생기는 교점의 개수를 그 즉시 업데이트 하여줌(전선 3개의 교점은 존재 x)
    # 교점을 구한 뒤에는 다음 반복에서도 비교를 하기 위해 바로 append로 추가시켜줌
    for n in range(N):
        list_ab = list(map(int,input().split()))
        for line in list_n:
            if line[0] < list_ab[0] and line[1] > list_ab[1]:
                result += 1
            elif line[0] > list_ab[0] and line[1] < list_ab[1]:
                result += 1
        list_n.append(list_ab)

    print(f'#{t+1} {result}')
