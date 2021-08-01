# 입력 받은 값을 2차원 리스트 형태로 저장
list_n = []
for i in range(4):
    sample = list(map(int, input().split()))
    list_n.append(sample)

# 좌표평면을 2차원 리스트에 표현 (0으로 초기화)
list_xy = []
for x in range(100):
    sample = []
    for y in range(100):
        sample.append(0)
    list_xy.append(sample)


# 입력받은 2차원 리스트의 각각의 index가 x 와 y라는 점을 이용해 이를 반복문의 range를 활용하여 1을 채움
for n in list_n:
    for idx_x in range(n[0], n[2]):
        for idx_y in range(n[1], n[3]):
            list_xy[idx_x][idx_y] = 1

# 반복이 끝나면 1의 개수를 모두 count로 구해 출력
cnt = 0
for xy in list_xy:
    cnt += xy.count(1)

print(cnt)