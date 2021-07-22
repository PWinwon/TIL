T = int(input())


for i in range(T):
    N, M = map(int, input().split())
    #N*N 행렬 2차원 리스트로 생성
    list_n = []
    for j in range(N):
        a = []
        a = list(map(int, input().split()))
        list_n.append(a)
    #M*M의 데이터(죽인파리수)를 받아올 1차원 리스트 생성
    #길이는 (N-M+1)**2 >> 파리채가 타격할 수 있는 모든 경우의 수
    list_m = [0] * (N-M+1)**2
    idx_x = M
    idx_y = M
    idx_m = 0
    #2개의 반복문을 통해 파리채의 모서리 시작점 확인
    for x in range(N-M+1):
        for y in range(N-M+1):
            #2개의 반복문을 통해 파리채의 모서리 시작점으로 부터 M*M의 값을 받아와서 저장
            for p_x in range(x,idx_x):
                for p_y in range(y, idx_y):
                    list_m[idx_m] += list_n[p_x][p_y]
            #파리채 경우의 수에 대해 확인해볼 경로를 생각해보면서 변수 증감과 초기화
            idx_m += 1
            idx_y += 1
        idx_x += 1
        idx_y = M
    #반복문이 끝나면 출력 후 마무리
    print(f'#{i+1} {max(list_m)}')
