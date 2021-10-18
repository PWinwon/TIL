decode_table = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4',
    '5','6','7','8','9','+','/'
    ]
T = int(input())

# 입력받은 문자를 decode_table과 비교하여 그 index 값으로 변환(2진수)
# 2진수로 저장을 할때는 앞의 '0b'문자와 0으로 채워져야한다는 것을 고려하여 처리
# 2진수를 다시 8자리씩 나누어 chr을 이용해 디코딩

for i in range(T):
    string = input()
    result = ''
    final_result = ''
    for st in string:
        deco_str = ''
        for dt in range(len(decode_table)):
            if st == decode_table[dt]:
                deco_str += bin(dt)[2:]
                while True:
                    if len(deco_str) < 6:
                        deco_str = '0' + deco_str
                    else:
                        break
                result += deco_str
    for x in range(0, len(result), 8):
        final_result += chr(int(result[x:x+8],2))
    print(f'#{i+1} {final_result}')
