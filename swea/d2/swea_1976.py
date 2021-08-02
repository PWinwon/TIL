T = int(input())

for i in range(T):
    # 입력 받은 시와 분의 데이터에 대해 각각 더해서 시와 분의 특성에 따라
    # 분이 60을 넘었을 때와 시가 12를 넘었을때에 대해 처리해줌
    hour1, minu1, hour2, minu2 = map(int, input().split())
    result_hour = hour1 + hour2
    result_minu = minu1 + minu2
    if result_minu > 60:
        result_minu -= 60
        result_hour += 1
    if result_hour >= 13:
        result_hour -= 12
    print(f'#{i+1} {result_hour} {result_minu}')