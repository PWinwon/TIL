N = int(input())

for n in range(1,N+1):
    idx = 0
    play = n
    while(n):
        if (n % 10 == 3) or (n % 10 == 6) or (n % 10 == 9):
            idx += 1
        n = n // 10
    if idx :
        play = '-' * idx
    
    print(play, end=' ')
