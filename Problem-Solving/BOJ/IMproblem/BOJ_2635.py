n = int(input())

len_max = 0
result = []

# 입력받은 n에 대하여 반복문 실행
for i in range(n+1):
    sample = []
    # 입력받은 n 과 반복문의 변수 i 를 순서대로 append
    sample.append(n)
    sample.append(i)
    idx = 1
    # 반복문을 돌며 문제의 조건에 맞추어 리스트를 채우고 값이 음수이면 그대로 break
    while True:
        x = sample[idx-1] - sample[idx]
        if x < 0:
            break
        else:
            sample.append(x)
            idx += 1
    # 생성된 sample의 길이가 len_max보다 길면 그값을 다시 저장
    if len_max <= len(sample):
        len_max = len(sample)
        result = sample
# 출력
print(len_max)
for j in range(len_max):
    if j == len_max-1:
        print(result[j], end='')
    else:
        print(result[j], end =' ')
