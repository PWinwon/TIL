T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    list_k = list(map(int, input().split()))
    # 전체 학생을 모두 담은 list_stu 리스트를 생성
    list_stu = list(range(1,N+1))
    list_no = []
    print(f'#{i+1}', end = '')
    # 전체 학생의 리스트의 원소를 반복문에 이용함
    for n in list_stu:
        # n (학생 번호) 가 list_k (과제 제출명단)에 없으면 출력
        if n not in list_k:
            print(f' {n}', end = '')
    print('')
