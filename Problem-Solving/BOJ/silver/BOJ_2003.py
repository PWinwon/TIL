'''
투포인터 left와 rigth를 이용해 해결
'''

N, M = map(int, input().split())
lst = list(map(int, input().split()))
# 리스트의 첫번째 칸을 부분합의 시작으로 설정
result = 0
left = 0
right = 1
temp = lst[left]
# 인덱스가 리스트의 범위가 넘어가지 않도록 조절하면서 진행
while left < N:
    # 부분합이 문제 요구의 M과 같을때 결과 값 +1 그리고 왼쪽 포인터를 1증가시켜 옮겨줌
    # 부분합에서 이전의 값도 빼줌
    if temp == M:
        result += 1
        temp -= lst[left]
        left += 1
    if right == N and temp < M:
        break
    # 문제에서 주어진 M에대해 크고 작은 상황에 대해서는 따로 처리를 해서 실행시간을 단축시킨다.
    elif temp < M:
        temp += lst[right]
        right += 1
    elif temp > M:
        temp -= lst[left]
        left += 1
print(result)