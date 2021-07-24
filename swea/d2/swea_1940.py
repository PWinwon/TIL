T = int(input())

for i in range(T):
    N = int(input())
    speed = 0
    location = 0
    for n in range(N):
        sb = input()
        if sb[0] == '0':
            p_m_z = 0
        else:
            p_m_z, num = map(int, sb.split())
        if p_m_z == 1:
            speed += num
        elif p_m_z == 2:
            speed -= num
        else:
            pass
        if speed > 0:
            location += speed
        else:
            speed = 0
    print(f'#{i+1} {location}')