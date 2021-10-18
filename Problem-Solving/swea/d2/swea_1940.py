T = int(input())

# 입력되는 값에 따라 처리를 함
# 물리적인 속도의 증감이 아닌 위치를 옮겨주는 방법으로 처리함
# 입력되는 값의 길이가 불규칙적이므로 그에 따른 처리를 하여줌
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