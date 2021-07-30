# 회문인지 검사해주는 함수(리스트, 문자열 둘다 확인가능)
def palindrome_check(words):
    while len(words) >= 0:
        if len(words) <= 1:
            return True
        if words[0] == words[-1]:
            words = words[1:-1]
        else:
            return False

for i in range(1, 11):
    N = int(input())
    list_n = []
    for j in range(8):
        sample_list = []
        sample_str = input()
        # 입력 받는 문자열이 붙어있어서 extend로 넣어주면서 각 문자로 분리해서 2차원 리스트로 저장
        sample_list.extend(sample_str)
        list_n.append(sample_list)
    result = 0
    for idx in range(8):
        for st in range(8-N+1):
            # 가로줄은 문자열로 슬라이싱해서 바로 넣어줌
            result += palindrome_check(list_n[idx][st:st+N])
            sero = []
            #세로줄은 2차원리스트의 인덱스로 접근하여 함수 호출
            for y in range(st, st+N):
                sero.append(list_n[y][idx])
            result += palindrome_check(sero)

    
    print(f'#{i} {result}')

