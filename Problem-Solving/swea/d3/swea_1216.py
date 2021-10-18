def palindrome_check(words):
    while True:
        if len(words) <= 1:
            return True
        if words[0] == words[-1]:
            words = words[1:-1]
        else:
            return False

for i in range(10):
    t = int(input())
    list_n = []
    for j in range(100):
        sample_list = []
        sample_str = input()
        sample_list.extend(sample_str)
        list_n.append(sample_list)
    # 길이가 1인 문자열은 무조건 회문이므로 max_lengh = 1 로 초기화
    max_length = 1
    # list_nt는 list_n의 전치행렬을 zip함수를 이용해 구해줌
    list_nt = list(zip(*list_n))
    # 길이가 긴 문자열부터 비교해서 회문이 나오면 그순간 break 길이가 더 짧은 문자열이 회문인지 검사할 필요 x
    for ll in range(100,1,-1):
        if max_length >= ll:
            break
        # 회문인지 확인할때 슬라이싱하기 위한 idx의 반복문
        for idx in range(100-ll+1):
            # 각 2차원 리스트의 한줄씩 뽑아내기 위함
            for n in list_n:
                # 회문인지 판별후 회문이라면 max_length 에 문자열 길이 ll 을 저장후 break
                if palindrome_check(n[idx:idx+ll]):
                    max_length = ll
                    break
            for nt in list_nt:
                if  palindrome_check(nt[idx:idx+ll]):
                    max_length = ll
                    break
    print(f'#{t} {max_length}')