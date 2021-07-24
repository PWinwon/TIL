T = int(input())

for i in range(T):
    P, Q, R, S, W = map(int, input().split())
    case_A = P * W
    if R > W:
        case_B  = Q
    else:
        case_B = Q + S * (W - R)
    
    if case_A <= case_B:
        print(f'#{i+1} {case_A}')
    else:
        print(f'#{i+1} {case_B}')