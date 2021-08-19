#########################################################
# 0817
#########################################################
# GNS 교수님 풀이
#
# lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# T = int(input())
#
# for tc in range(1, T + 1) :
#     tmp , N = input().rstrip().split()
#     N = int(N) # N 개의 단어가 입력
#     word_lst = input().split() # 띄어쓰기 단위로 입력 후 리스트화
#
#     print("#{}".format(tc))
#     for i in range(len(lst)):
#         lst[i] # "ZRO" "ONE" "TWO" "THR" "FOR" .... 순서로 선택
#         # word_lst 에서 lst1[i] 같은거 찾기
#         for j in range(N):
#             #word_lst[j] vs lst[i]
#             if word_lst[j] == lst[i] :
#                 print(lst[i] ,end = ' ')

#########################################################
# 문자열 비교

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
# test_case = int(input())
#
# for tc in range(test_case):
#     str1 = input()
#     str2 = input()
#     N = len(str1)
#     M = len(str2)
#     print('#{} {}'.format(tc+1, find_pattern(str2, str1, M, N)))

#########################################################
# 문자열 비교 - 교수님 풀이

# def is_same(start_idx, str1, str2) :
#     n = len(str1)
#     if start_idx + n - 1 >= len(str2) : return 0
#     for i in range(n) :
#         if str1[i] != str2[start_idx + i] :
#             return 0
#     return 1
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     str1 = input()
#     str2 = input()
#     flag = 0
#     for i in range(len(str2)):
#         ret = is_same(i, str1,str2)
#         if ret == 1:
#             flag = 1
#             break
#
#     if flag == 0:
#         print("#{} 0".format(tc))
#     else :
#         print("#{} 1".format(tc))

#########################################################
# 회문
#
# def rotation_sentence(lst, n, m):
#     for st in range(n - m + 1):
#         lst_chk = lst[st:st+m]
#         str1 = lst[st:st+m]
#         while True:
#             if len(lst_chk) < 2:
#                 return str1
#             if lst_chk[0] == lst_chk[-1]:
#                 lst_chk = lst_chk[1:-1]
#             else:
#                 break
#     return False
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N, M = map(int, input().split())
#     lst_n = [input() for _ in range(N)]
#     for r in range(N):
#         if rotation_sentence(lst_n[r], N, M):
#             result = rotation_sentence(lst_n[r], N, M)
#         lst_sero = ''
#         for c in range(N):
#             lst_sero += lst_n[c][r]
#         if rotation_sentence(lst_sero, N, M):
#             result = rotation_sentence(lst_sero, N, M)
#             break
#     print('#{} {}'.format(tc+1, result))

#########################################################
# 회문 - 교수님 풀이

# def is_palindrome(str_) :
#     n = len(str_)
#     for i in range(n) :
#         if str_[i] != str_[n-1-i]:
#             return 0
#     return 1
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N x N 2차원 리스트 / M 은 palindrome 길이
#     MAP = []
#     for y in range(N):
#         MAP.append(input())
#     # 가로 회문 검사
#     ans = ""
#     for y in range(N):
#         for x in range(N-M + 1):
#             temp_str = MAP[y][x:x+M]
#             ret = is_palindrome(temp_str) # O(M)
#             if ret == 1:
#                 ans = temp_str
#
#     # 세로 회문 검사
#     for x in range(N):
#         for y in range(N-M + 1):
#             temp_str = ""
#             # O(M)
#             for i in range(y, y + M):
#                 temp_str += MAP[i][x]
#             # O(M)
#             ret = is_palindrome(temp_str)
#             if ret == 1:
#                 ans = temp_str
#
#     print("#{} {}".format(tc, ans))

#########################################################
# 글자수

# test_case = int(input())
#
# for tc in range(test_case):
#     str_sm = input()
#     str_lng = input()
#
#     max_cnt = 0
#     for sm in range(len(str_sm)):
#         cnt = 0
#         for lng in range(len(str_lng)):
#             if str_lng[lng] == str_sm[sm]:
#                 cnt += 1
#         if max_cnt < cnt:
#             max_cnt = cnt
#
#     print('#{} {}'.format(tc+1, max_cnt))

#########################################################
# 글자수 - 교수님 풀이

# T = int(input())
#
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#     max_cnt = 0
#     for i in range(len(str1)):
#         str1[i]
#         cnt = 0
#         for j in range(len(str2)):
#             if str1[i] == str2[j] :
#                 cnt += 1
#
#         if max_cnt < cnt :
#             max_cnt = cnt
#
#     print("#{} {}".format(tc, max_cnt))

#########################################################
# 가장 빠른 문자열 타이핑

# test_case = int(input())
#
# for tc in range(test_case):
#     A, B = input().split()
#     a_len = len(A)
#     b_len = len(B)
#
#     idx_a = 0
#     cnt = 0
#     while idx_a < a_len:
#         if A[idx_a] == B[0]:
#             if A[idx_a:idx_a+b_len] == B:
#                 cnt += 1
#                 idx_a += b_len
#             else:
#                 cnt += 1
#                 idx_a += 1
#         else:
#             cnt += 1
#             idx_a += 1
#
#     print('#{} {}'.format(tc+1, cnt))

#########################################################
# 가장 빠른 문자열 타이핑- 교수님 풀이
#
# def is_same(start_idx, n):
#     if start_idx + n - 1 >= len(A) : return 0
#     for i in range(n) :
#         if A[start_idx +i] != B[i]:
#             return 0
#     return 1
#
# T = int(input())
# for tc in range(1, T + 1) :
#     A ,B = input().rstrip().split()
#     i = 0 # 비교시작인덱스
#     n = len(A)
#     cnt = 0 # 타이핑 횟수
#     while i < n:
#         ret = is_same(i,len(B)) # 같으면 단축키 사용
#         if ret == 1: # 단축키 사용가능
#             i += len(B)
#             cnt += 1
#         else :
#             i += 1
#             cnt += 1
#     print("#{} {}".format(tc, cnt))


#########################################################
# 쇠막대기 자르기
#
# test_case = int(input())
#
# for tc in range(test_case):
#     lst_n = input()
#     n_len = len(lst_n)
#     cnt = 0
#     total = 0
#     for idx in range(n_len):
#         if lst_n[idx] == '(' and lst_n[idx+1] == ')':
#             total += cnt
#         elif lst_n[idx] == '(':
#             total += 1
#             cnt += 1
#         elif lst_n[idx] == ')' and lst_n[idx-1] != '(':
#             cnt -= 1
#
#     print('#{} {}'.format(tc+1, total))

#########################################################
# 쇠막대기 자르기 - 교수님 풀이

# T = int(input())
#
# for tc in range(1, T+1) :
#     s = input()
#     ans = 0
#     n = len(s)
#     i = 0
#     open_cnt = 0
#     while i < n:
#         # laser
#         if i+1 < n and s[i] == '(' and s[i + 1] == ')':
#             ans += open_cnt
#             i += 2
#         elif s[i] == '(':
#             open_cnt += 1
#             i += 1
#         elif s[i] == ')': #꼬다리 개수 카운트
#             ans += 1
#             open_cnt -= 1
#             i += 1
#
#     print("#{} {}".format(tc, ans))
#########################################################
# 회문 2
# def palindrome_check(words):
#     while True:
#         if len(words) <= 1:
#             return True
#         if words[0] == words[-1]:
#             words = words[1:-1]
#         else:
#             return False
#
# for i in range(10):
#     t = int(input())
#     list_n = [input() for _ in range(100)]
#     max_length = 1
#     list_nt = list(zip(*list_n))
#     for ll in range(100,1,-1):
#         if max_length >= ll:
#             break
#         for idx in range(100-ll+1):
#             for n in list_n:
#                 if palindrome_check(n[idx:idx+ll]):
#                     max_length = ll
#                     break
#             for nt in list_nt:
#                 if palindrome_check(nt[idx:idx+ll]):
#                     max_length = ll
#                     break
#     print(f'#{t} {max_length}')
