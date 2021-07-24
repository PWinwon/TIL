T = int(input())

for i in range(T):
    hour1, minu1, hour2, minu2 = map(int, input().split())
    result_hour = hour1 + hour2
    result_minu = minu1 + minu2
    if result_minu > 60:
        result_minu -= 60
        result_hour += 1
    if result_hour >= 13:
        result_hour -= 12
    print(f'#{i+1} {result_hour} {result_minu}')