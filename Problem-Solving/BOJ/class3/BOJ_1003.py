arr = [[0, 0] for _ in range(41)]

for i in range(41):
    if i == 0:
        arr[i][0] = 1
        arr[i][1] = 0
    elif i == 1:
        arr[i][0] = 0
        arr[i][1] = 1
    else:
        arr[i][0] = arr[i-2][0] + arr[i-1][0]
        arr[i][1] = arr[i-2][1] + arr[i-1][1]

T = int(input())

for tc in range(T):
    N = int(input())
    print(arr[N][0], arr[N][1])