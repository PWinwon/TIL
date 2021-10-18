test_case = int(input())

# 규칙에 따라 초기화된 상태에서 메모리를 복구하는데 걸린 횟수
# --> 0 >> 1 or 1 >> 0 으로 변화가 몇번 이루어졌나?
# 주의점 : 0으로 시작할 때와 1로 시작할때 cnt 횟수에 대해 신경써 줘야함
# 바뀌는 기준, index를 증가시키며 비교를 진행할때 이전의 문자와 달라지는 경우
for tc in range(test_case):
    binarys = input()
    if binarys[0] == '0':
        cnt = 0
    else:
        cnt = 1
    for bi in range(1, len(binarys)):
        if binarys[bi] != binarys[bi-1]:
            cnt += 1
    if int(binarys) == 0:
        cnt = 0
    print('#{} {}'.format(tc+1, cnt))
