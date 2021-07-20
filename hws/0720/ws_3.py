number = int(input())

for i in range(1, number+1):
    k = 1
    while k <= i:
        print(k, end=' ')
        k += 1
    print('')