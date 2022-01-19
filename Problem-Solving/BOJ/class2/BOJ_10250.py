T = int(input())

for tc in range(T):
    R, C, N = map(int, input().split())
    result1 = 1
    result2 = 1
    if N % R:
        result1 = (N % R) * 100
        result2 += N // R
    else:
        result1 = R * 100
        result2 = N // R


    print(result1 + result2)