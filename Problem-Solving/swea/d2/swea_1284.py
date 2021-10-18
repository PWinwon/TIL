T = int(input())

for i in range(T):
    P, Q, R, S, W = map(int, input().split())
    # A사의 요금 경우 계산
    case_A = P * W
    # B사의 요금 경우 계산
    if R > W:
        case_B  = Q
    else:
        case_B = Q + S * (W - R)
    
    # 조건문을 통해 가격이 저렴한 결과 출력
    if case_A <= case_B:
        print(f'#{i+1} {case_A}')
    else:
        print(f'#{i+1} {case_B}')