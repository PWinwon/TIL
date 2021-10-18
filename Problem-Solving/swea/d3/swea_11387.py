test_case = int(input())

# 데미지의 변화에 대한 수식을 반복문을 통해 누적시키는 방식으로 해결
# 주의점 : 첫 공격은 추가량이 없으므로, 반복문의 시작을 신경써서 작성해 주어야함
# 정답은 정수형으로 출력해야 함을 주의
for tc in range(test_case):
    d, l, n = map(int, input().split())
    damage = 0
    for cnt in range(0, n):
        damage += d*(1 + cnt * l * 0.01)
    
    print('#{} {}'.format(tc+1, int(damage)))