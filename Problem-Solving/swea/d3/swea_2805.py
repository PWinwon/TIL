T = int(input())

for i in range(T):
    N = int(input())
    list_n = []
    # 입력받는 밭의 상태가 연속된 숫자로 입력되어서 일단 문자열로 입력받음
    # list_n 은 1차원 리스트
    for n in range(N):
        sample_list = input()
        list_n.append(sample_list)
    # 리스트의 index를 제어하기 위해 변수 생성
    idx_x = N // 2
    j = 1
    pl_mn = 0
    result = 0
    for ln in list_n:
        # 지정된 문자열에 마름모 모양으로 슬라이싱하여 정수형으로 저장
        num = int(ln[idx_x-pl_mn:idx_x+pl_mn+1])
        # 각 자릿수 result에 누적합
        while num:
            result += num % 10
            num = num // 10
        # 마름모의 중간에 도착하면 다시 값이 줄어들기 위한 변수 조절
        if idx_x == pl_mn:
            j *= -1
        # 다음 배열에서의 수확량 변화를 위한 변수조절
        pl_mn += j
    print(f'#{i+1} {result}')