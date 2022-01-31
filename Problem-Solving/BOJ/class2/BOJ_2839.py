N = int(input())

result = 0

while True:
    if N % 5 == 0:
        result += (N//5)
        print(result)
        break

    N -= 3
    result += 1

    if N < 0:
        print(-1)
        break