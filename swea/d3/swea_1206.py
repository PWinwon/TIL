
for i in range(1,11):
    # 케이스 길이와 리스트 입력
    T_length = int(input())
    view_list = list(map(int, input().split()))
    #view가 보장된 세대를 확인하기위한 변수 선언
    view_ok = 0
    check_list = [0] * 4
    #index를 고려해 반복문 범위를 설정해서 view가 확보된 세대를 알아볼 건물을 기준으로 반복문 실행
    for vi in range(2, T_length-2):
        idx_ck = 0
        #view가 확보된 세대를 알아볼 건물을 기준으로 양 2개의 건물과의 차이를 연산해 check_list에 저장
        for j in range(vi-2,vi+3):
            if vi == j:
                pass
            else:
                check_list[idx_ck] = view_list[vi] - view_list[j]
                idx_ck += 1
        #check_list에 min함수를 이용해 0보다 크면(주위에 자신보다 큰 건물이 없으면) view_ok변수에 더해줌
        if min(check_list) > 0:
            view_ok += min(check_list)
    #반복이 끝나면 출력후 종료
    print(f'#{i} {view_ok}')