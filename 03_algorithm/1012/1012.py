# 1이 연속한 최대길이 출력 + 그 중 제일 시작인덱스가 작은거 출력 - 교수님 풀이

# lst = list(map(int, list("000011000110111011111100001100011111100001010111")))
# de = - 1
# i = 0
# max_length = 0
# max_start = -1
# while i < len(lst) :
#     if lst[i] == 1:
#         a = i
#         cnt = 0
#         while a < len(lst) and lst[a] == 1 :
#             cnt += 1
#             a += 1
#         if max_length < cnt:
#             max_start = i
#             max_length = cnt
#         i = a + 1
#
#     else :
#         i += 1
#
# print("{} {}".format(max_length , max_start))



