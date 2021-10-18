T = int(input())

for i in range(T):
    N = int(input())
    list_n = list(map(int, input().split()))
    # 결과를 받을 result 리스트 생성 및 초기화
    result = [0] * N
    # 입력받은 리스트의 원소를 하나씩 꺼내 비교
    for ln in list_n:
        # 결과를 출력할 result의 index 값을 알려줄 변수 idx생성
        idx = 0
        # ln과 나머지 원소들을 비교하며 ln보다 작은 값이 있다면 idx += 1
        for x in range(N):
            if ln > list_n[x]:
                idx += 1
        # ln과 같은 값이 있을 경우 그 다음 칸에 저장하기 위해 while 문을 이용해 idx 값 조절
        while(True):
            if result[idx] == 0:
                result[idx] = ln
                break
            else:
                idx += 1
    # 결과 출력
    print(f'#{i+1}', end = ' ')
    for re in range(N):
        # 결과 출력이 끝나면 줄바꿈을 위한 조건문 
        if re == N-1:
            print(result[re])
        else:
            print(result[re], end = ' ')
