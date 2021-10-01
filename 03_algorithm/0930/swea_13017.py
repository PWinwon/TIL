# T = int(input())
#
# for tc in range(T):
#     N = float(input())
#     result = ''
#     for i in range(1, 14):
#         N *= 2
#         if N >= 1:
#             result += '1'
#             N -= 1
#         else:
#             result += '0'
#         if N == 0:
#             break
#     if N:
#         print('#{} overflow'.format(tc+1))
#     else:
#         print('#{} {}'.format(tc+1, result))


##################################################################
## 교수님 풀이

# import sys
#
# sys.stdin = open("text.txt", "r")
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = float(input())
#     s = '' # 뽑아낸거를 붙여가기
#     cnt = 0  # 뽑은거의 개수 세기
#
#     # N > 0, cnt <= 12
#     while N > 0 and cnt <= 12 :
#         N *= 2
#         cnt += 1
#
#         if N >= 1 :
#             s += '1'
#             N -= 1
#         else:
#             s += '0'
#
#     #  N = 0 이거나 cnt > 12
#     if cnt > 12 :
#         print("#{} overflow".format(tc))
#     else:
#         print("#{} {}".format(tc, s))


##############################################################
# 풀이 2 재귀를 이용한 자료구조 생성


def func(level, sum , bits) : #sum(float로 계산) , bits는 1또는 0을 붙여나간다
    if level == 13:
        #print(sum, ":" , bits)
        MAP[str(sum)] = bits
        return

    func(level + 1, sum + (0.5) ** level, bits + '1') # 현재 level bit를 선택 o
    func(level + 1, sum, bits + '0') # 현재 level bit를 선택 x


def erase_zero(s):
    lst = []
    check = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            check = 1
        if check == 1:
            lst.append(s[i])

    ret = ""
    while lst:
        ret += lst.pop()

    return ret


MAP = dict()
func(1, 0, '')
de = - 1

T = int(input())
for tc in range(1, T + 1):
    key = input()
    if key in MAP:
        val = MAP[key]
        val = erase_zero(val)
        print("#{} {}".format(tc, val))
    else:
        print("#{} overflow".format(tc))