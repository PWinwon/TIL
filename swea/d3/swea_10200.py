T = int(input())

for i in range(T):
    N, A, B = map(int, input().split())
    max_sub = min(A,B)
    min_sub = (A + B) - N
    if min_sub < 0:
        min_sub = 0

    print(f'#{i+1} {max_sub} {min_sub}')