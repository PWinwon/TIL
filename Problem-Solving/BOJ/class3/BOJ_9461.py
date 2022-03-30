wave_lst = [0] * 101

wave_lst[0] = 1
wave_lst[1] = 1
wave_lst[2] = 1

for i in range(3, 100):
    wave_lst[i] = wave_lst[i-3] + wave_lst[i-2]

T = int(input())

for tc in range(T):
    N = int(input())
    print(wave_lst[N-1])