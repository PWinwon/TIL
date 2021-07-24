T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    # 입력 받는 각각의 문자열의 길이를 비교하여
    # 길이에 따라 각각의 리스트에 저장
    if A > B:
        l_l = A
        l_s = B
        list_long = list(map(int, input().split()))
        list_short = list(map(int, input().split()))
    else:
        l_s = A
        l_l = B
        list_short = list(map(int, input().split()))
        list_long = list(map(int, input().split()))
    result = []
    # 긴 리스트를 따라서 짧은 리스트가 이동하며 모든경우의 수를 고려하여
    # 각각의 곱에 대한 합을 result 리스트에  append로 저장
    for x in range(l_l - l_s + 1):
        val = 0
        for s in range(l_s):
            val += list_long[x+s] * list_short[s]
        result.append(val)
    # 출력시 max를 사용하여 그 중 가장 큰 값 출력
    print(f'#{i+1} {max(result)}')
