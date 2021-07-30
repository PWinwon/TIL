table_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for i in range(T):
    t, N = input().split()
    N = int(N)
    list_n = list(input().split())
    # 입력받은 문자열 리스트(list_n)의 원소에 대해
    # table_num과 비교하여 table_num의 값과 같을 때 그 index의 값으로 치환시켜줌
    for n in range(N):
        for idx in range(10):
            if list_n[n] == table_num[idx]:
                list_n[n] = idx
                break
    # 각 원소를 index 값으로 바꾸어 주었으므로 sort()를 이용해 정렬
    list_n.sort()
    print(f'{t}')
    # 정렬된 list_n에 대해 그 값에 해당 index에 해당하는 table_num을 출력
    for n in range(N):
        for idx in range(10):
            if list_n[n] == idx:
                print(f'{table_num[idx]}', end = ' ')
                break
    print('')
    
    