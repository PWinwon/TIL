T = int(input())
for t in range(T):
    D, A, B, F = map(int, input().split())
    print(f'#{t+1} {(D / (A+B)) * F}')