#########################################################
# 함수 작성 연습
#
# def is_same(a, b):
#     if len(a) != len(b):
#         return 0
#     for idx in range(len(a)):
#         if a[idx] != b[idx]:
#             return 0
#     return 1
#
#
# lst1 = [3, 2, 7, 5, 8, 9]
# lst2 = list(map(int, input().split()))
# result = is_same(lst1, lst2)
#
# if result:
#     print('동일')
# else:
#     print('안동일')

#########################################################
# 함수 작성 연습2

# def is_exist(target):
#     for r in range(len(lst)):
#         for c in range(len(lst[r])):
#             if target == lst[r][c]:
#                 return 1
#     return 0
#
# lst = [
#     [3, 2, 7, 9],
#     [5, 1, 2, 5],
#     [1, 2, 3, 4],
#     ]
# result = is_exist(1)
#
# if result:
#     print('존재')
# else:
#     print('안존재')

#########################################################
# 앞글자 따기
# def first_char(sentense):
#     return sentense[0].upper()
#
#
# test_case = int(input())
#
# for tc in range(test_case):
#     n = int(input())
#     lst_n = list(input().split())
#     result = ''
#     for chars in range(n):
#         result += first_char(lst_n[chars])
#     print('#{} {}'.format(tc+1, result))


#########################################################
# 문자열의 거울상

# original_char = ['b', 'd', 'p', 'q']
# mirror_char = ['d', 'b', 'q', 'p']
#
# test_case = int(input())
#
# for tc in range(test_case):
#     sentence = input()
#     sentence = sentence[::-1]
#     result = ''
#     for sen in sentence:
#         for idx in range(4):
#             if sen == original_char[idx]:
#                 result += mirror_char[idx]
#
#     print('#{} {}'.format(tc+1, result))

#########################################################
# 모음이 보이지 않는 사람

# moum_lst = ['a', 'e', 'i', 'o', 'u']
#
# test_case = int(input())
#
# for tc in range(test_case):
#     sentence = input()
#     result = ''
#     for sen in sentence:
#         sample = sen
#         for mo in range(5):
#             if sen == moum_lst[mo]:
#                 sample = ''
#         result += sample
#     print('#{} {}'.format(tc+1, result))

#########################################################
# 모음이 보이지 않는 사람 - 교수님 풀이
#
# moum = [ 'a','e','i','o','u']
#
# is_moum = [0 for _ in range(201)] # 0 ~ 200
# for i in range(5):
#     val = ord(moum[i]) # 97 101 105 111 117
#     is_moum[val] = 1
#
# s = input()
# for i in range(len(s)):
#     val = ord(s[i]) # ord('a')
#     if is_moum[val] == 0:
#         print(chr(val), end = '')

#########################################################
# 2차원 리스트에서 패턴 찾기

# lst = [
#     [3, 2, 7, 9],
#     [5, 1, 2, 3],
#     [3, 2, 7, 9],
#     [3, 2, 7, 9],
#     [1, 2, 3, 4],
#     [4, 3, 2, 1],
# ]
# pattern = [3, 2, 7, 9]
# result = 0
# for r in range(6):
#     cnt = 0
#     for c in range(4):
#         if lst[r][c] == pattern[c]:
#             cnt += 1
#         else:
#             break
#     if cnt == 4:
#         result += 1
# print(result)

#########################################################
# 2차원 리스트에서 패턴 찾기 - 교수님 풀이

# def is_same(y ,a ,b): # y층이랑 패턴이랑 검사
#     # apart[y] vs pattern
#     for i in range(4):
#         if a[y][i] != b[i]:
#             return 0
#
#     return 1
#
# apart = [
#     [3,2,7,9],
#     [5,1,2,3],
#     [3,2,7,9],
#     [3,2,7,9],
#     [1,2,3,4],
#     [4,3,2,1]
# ]
#
# pattern = [3,2,7,9]
# cnt = 0
# for row in range(6):
#     ret = is_same(row, apart, pattern)
#     if ret == 1:
#         cnt += 1
#
# print(cnt)

#########################################################
# 1차원 리스트 (실패)

# def is_pattern(a, p):
#     idx = len(p) - 1
#     result = 0
#     while idx < len(a):
#         cnt = 0
#         if a[idx] == p[len(p)-1]:
#             for i in range(len(p)-1):
#                 if a[idx-len(p) + i + 1] == p[i]:
#                     cnt += 1
#             if cnt == len(p) - 1:
#                 result += 1
#         elif a[idx] in p:
#             for i in range(len(p)):
#                 if a[idx] == p[i]:
#                     idx += len(p) - 1 - i
#         else:
#             idx += len(p)
#     return result
#
# lst = [7, 1, 2, 5, 3, 2, 7, 9, 1, 2, 5]
# pattern = [1, 2, 5]
#
# re = is_pattern(lst, pattern)
# print(re)

#########################################################
# 1차원 리스트 - 교수님 풀이
# def is_pattern(start_idx, pn):
#     if start_idx + pn -1 >= len(lst): return 0 # 인덱스 초과 방지
#     for i in range(pn):
#         # lst[start_idx + i] vs pattern[i]
#         if lst[start_idx + i ] != pattern[i]:
#             return 0
#
#     return 1
#
# lst = [7,1,2,5,3,2,7,9,1,2,5]
# pattern = [1,2,5]
#
# cnt = 0
# for i in range(len(lst)):
#     ret = is_pattern(i, 3)
#     if ret == 1:
#         cnt += 1
#
# print(cnt)


#########################################################
# String

# def find_pattern(a, p, al, pl):
#     result = 0
#     for idx in range(al):
#         idx_p = 0
#         cnt = 0
#         if a[idx] == p[idx_p]:
#             while idx + idx_p < al and cnt < pl:
#                 if a[idx+idx_p] == p[idx_p]:
#                     cnt += 1
#                     idx_p += 1
#                 else:
#                     break
#             if cnt == pl:
#                 result += 1
#
#     return result
#
#
# for tc in range(10):
#     test_case = int(input())
#     pattern = input()
#     sentence = input()
#
#     p_len = len(pattern)
#     s_len = len(sentence)
#
#     total = find_pattern(sentence, pattern, s_len, p_len)
#     print('#{} {}'.format(test_case, total))

#########################################################
# GNS

# gns_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
# test_case = int(input())
#
# for tc in range(test_case):
#     tcase, N = input().split()
#     lst_n = list(input().split())
#     N = int(N)
#     num_lst = [0] * 10
#
#     for n in range(N):
#         for gn in range(10):
#             if lst_n[n] == gns_lst[gn]:
#                 num_lst[gn] += 1
#                 break
#     cnt = 0
#     for idx in range(10):
#         for _ in range(num_lst[idx]):
#             lst_n[cnt] = gns_lst[idx]
#             cnt += 1
#
#     print('{}'.format(tcase))
#     for i in range(N):
#         print(lst_n[i], end=' ')
#     print('')