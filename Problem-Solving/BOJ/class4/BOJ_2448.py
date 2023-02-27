import sys

input = sys.stdin.readline

N = int(input().strip())

stars = [[' ']*2*N for _ in range(N)]

def my_func(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i+1][j-1] = '*'
        stars[i+1][j+1] = '*'
        for k in range(-2, 3):
            stars[i+2][j-k] = '*'

    else:
        newSize = size//2
        my_func(i, j, newSize)
        my_func(i+newSize, j-newSize, newSize)
        my_func(i+newSize, j+newSize, newSize)

    return

my_func(0, N-1, N)

for star in stars:
    print(''.join(star))