# ------------------------------------------------------------
# 0812
# ------------------------------------------------------------

###################################################################
## flatten DAT 이용


# for tc in range(1, 11):
#     dump = int(input())
#     lst_n = list(map(int, input().split()))
#     lst_idx = [0] * 101
#
#     for i in range(100):
#         lst_idx[lst_n[i]] += 1
#     # print(lst_idx)
#     min_idx = 0
#     max_idx = 0
#     gap = 0
#     while True:
#         for min_x in range(101):
#             if lst_idx[min_x] > 0:
#                 min_idx = min_x
#                 lst_idx[min_x] -= 1
#                 lst_idx[min_x+1] += 1
#                 break
#         for max_x in range(100, -1, -1):
#             if lst_idx[max_x] > 0:
#                 max_idx = max_x
#                 lst_idx[max_x] -= 1
#                 lst_idx[max_x-1] +=1
#                 break
#         if dump == 0:
#             gap = max_idx - min_idx
#             break
#         dump -= 1
#
#     print('#{} {}'.format(tc, gap))


#########################################################
# 색칠하기
# test_case = int(input())
#
# for tc in range(test_case):
#     N = int(input())
#     lst_map = [[0] * 10 for _ in range(10)]
#     lst_n = []
#     for n in range(N):
#         lst_n.append(list(map(int, input().split())))
#
#     cnt = 0
#     for n in range(N):
#         for r in range(lst_n[n][0], lst_n[n][2] + 1):
#             for c in range(lst_n[n][1], lst_n[n][3] + 1):
#                 lst_map[r][c] = lst_map[r][c] | lst_n[n][4]
#
#     for r in range(10):
#         for c in range(10):
#             if lst_map[r][c] == 3:
#                 cnt += 1
#
#     print('#{} {}'.format(tc+1, cnt))

#########################################################
# 부분집합의 합

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# test_case = int(input())
#
#
# for tc in range(test_case):
#     N, K = map(int, input().split())
#     result = 0
#     for a in range(1<<12):
#         total = 0
#         cnt = 0
#         for i in range(12):
#             if a & (1<<i):
#                 total += A[i]
#                 cnt += 1
#         if total == K and cnt == N:
#             result += 1
#
#     print('#{} {}'.format(tc+1, result))

#########################################################
# 디버깅 퀘스트

# def kfc():
#     print("K")
#     print("F")
#     print("C")
#
#
# # break point
# x = 1
# x = 2
# x = 3
# x = 4
# x = 5
# # run to cursor -> step over
# x = 10
# x = 20
# x = 30
# x = 40
#
# # step into
# kfc()
# print("i'm return")
# x = -1
# x = -2
# x = -3
# # finish
# x = 5
# x = 7
# x = 99

#########################################################
# 디버깅 퀘스트2
# def over():
#     for i in range(10):
#         print("#", end = '')
#     print("OVER")
#
# def into():
#     print("INTO")
#
# over() #over
# into() #into
# over()
# over()
# over()
# into()
# over()
# into()
# over()
# into()
# over()

#########################################################
# 디버깅 퀘스트3
# def gogo():
#     print("GOGO")
#     return
#
# def bts():
#     gogo()
#     print("BTS LAST")
#     return
#
# def abc():
#     bts()
#     gogo()
#     print("ABC LAST")
#     return
#
# gogo()
# abc()
# bts()
# print("ALL FINISH")

#########################################################
# 어디에 단어가 들어갈 수 있을까
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N, K = map(int, input().split())
#     lst_n = [list(map(int, input().split())) for _ in range(N)]
#
#     result = 0
#     for r in range(N):
#         cnt = 0
#         cnt2 = 0
#         for c in range(N):
#             if lst_n[r][c] == 1:
#                 cnt += 1
#             elif cnt == K:
#                 result += 1
#                 cnt = 0
#             else:
#                 cnt = 0
#
#             if lst_n[c][r] == 1:
#                 cnt2 += 1
#             elif cnt2 == K:
#                 result += 1
#                 cnt2 = 0
#             else:
#                 cnt2 = 0
#         if cnt == K:
#             result += 1
#             cnt = 0
#         else:
#             cnt = 0
#         if cnt2 == K:
#             result += 1
#             cnt2 = 0
#         else:
#             cnt2 = 0
#
#     print('#{} {}'.format(tc+1, result))

#########################################################
# 파리퇴치
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N, M = map(int, input().split())
#     lst_n = [list(map(int, input().split())) for _ in range(N)]
#
#
#     max_result = 0
#     for r in range(N-M+1):
#         for c in range(N-M+1):
#             kill_num = 0
#             for m_r in range(r, r+M):
#                 for m_c in range(c, c+M):
#                     kill_num += lst_n[m_r][m_c]
#             if max_result < kill_num:
#                 max_result = kill_num
#
#     print('#{} {}'.format(tc+1, max_result))

#########################################################
# 파리퇴치 -2 하드코딩 연습 구간합 중 최댓값 구하기
#
# def get_sum(start_idx, M):
#     sum = 0
#     for i in range(M): # [start_idx+ 0 1 2 3 .... M-1]
#         sum += lst[start_idx + i]
#
#     return sum
#
# lst = [3,2,7,5,9,8,7,2,1]
#
# N = 9 # lst 크기
# M = int(input())
# max_idx = -1
# max_sum = int(-21e8)
# for i in range(0,N - M + 1):
#     ret = get_sum(i,M)
#     if ret > max_sum:
#         max_sum = ret
#         max_idx = i # 시작인덱스
#
# print(max_idx , max_sum)

#########################################################
# 파리퇴치 -2 0을 포함하지 않는 모든 연속된 구간

# lst = [5, 2, 0, 7, 7, 0, 2, 1, 9]
#
# for i in range(9):
#     str_sam = []
#     cnt = 0
#     for j in range(i, 9):
#         if lst[j] == 0:
#             break
#         else:
#             str_sam.append(lst[j])
#             print(str_sam)

# 교수님 풀이
# lst = [5,2,0,7,7,0,2,1,9]
#
# for s in range(9):
#     for e in range(s,9):
#         # 1. 시작 ~ 끝 0 이있는가?
#         check = 0
#         for i in range(s, e + 1) :
#             if lst[i] == 0:
#                 check = 1
#
#         # 2. 0 이 없으면 출력하기
#         if check == 0 :
#             for i in range(s, e + 1) :
#                 print(lst[i] , end = ' ')
#             print()
# 교수님 풀이 2
# lst = [5,2,0,7,7,0,2,1,9]
#
# def is_zero_exist(s, e):
#     for i in range(s, e + 1):
#         if lst[i] == 0 :
#             return True # 0이 있다
#
#     return False # 0이 없다
#
# for s in range(9):
#     for e in range(s,9):
#         # 1. 시작 ~ 끝 0 이있는가?
#         check = is_zero_exist(s,e)
#         # 2. 0 이 없으면 출력하기
#         if check == 0 :
#             for i in range(s, e + 1) :
#                 print(lst[i] , end = ' ')
#             print()

#########################################################
# 파리퇴치 - 2 함수를 이용

# def get_sum(row,col,m):
#     result = 0
#     for ro in range(row, row+m):
#         for co in range(col, col+m):
#             result += lst_n[ro][co]
#     return result
#
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N, M = map(int, input().split())
#     lst_n = [list(map(int, input().split())) for _ in range(N)]
#     max_result = 0
#     for r in range(N-M+1):
#         for c in range(N-M+1):
#             kill_num = get_sum(r, c, M)
#             if max_result < kill_num:
#                 max_result = kill_num
#
#     print('#{} {}'.format(tc+1, max_result))


#########################################################
# 이진 탐색 (ICE BREAKING)

# lst = [1, 2, 5, 7, 9, 15, 17]
# left = 0
# right = 6
# target = 2
#
# while left <= right:
#     mid = (left + right) // 2
#     if target == lst[mid]:
#         print('찾았다')
#         break
#     if target < lst[mid]:
#         right = mid - 1
#     elif target > lst[mid]:
#         left = mid + 1


#########################################################
# 이진 탐색

# test_case = int(input())
# for tc in range(test_case):
#     P, A, B = map(int, input().split())
#     left = 1
#     right = P
#     a_cnt = 0
#     cnt = 0
#     while left < right:
#         mid = int((left+right)/2)
#         cnt += 1
#         if mid == A:
#             a_cnt = cnt
#             break
#         elif mid > A:
#             right = mid
#         else:
#             left = mid
#
#     left = 1
#     right = P
#     b_cnt = 0
#     cnt = 0
#     while left <= right:
#         mid = int((left+right)/2)
#         cnt += 1
#         if mid == B:
#             b_cnt = cnt
#             break
#         elif mid > B:
#             right = mid
#         else:
#             left = mid
#
#     if a_cnt < b_cnt:
#         print('#{} A'.format(tc+1))
#     elif a_cnt > b_cnt:
#         print('#{} B'.format(tc+1))
#     else:
#         print('#{} 0'.format(tc+1))


#########################################################
# 특별한 정렬 ( 선택 정렬 )

# test_case = int(input())
#
# for tc in range(test_case):
#     N = int(input())
#     a = list(map(int, input().split()))
#
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if i % 2 == 0:
#                 if a[i] < a[j]:
#                     a[i], a[j] = a[j], a[i]
#             else:
#                 if a[i] > a[j]:
#                     a[i], a[j] = a[j], a[i]
#
#     print('#{}'.format(tc+1), end='')
#     for idx in range(10):
#         print(' {}'.format(a[idx]), end='')
#     print('')


#########################################################
# 숫자를 정렬하자
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N = int(input())
#     lst_n = list(map(int, input().split()))
#
#     for i in range(N-1):
#         for j in range(i,N):
#             if lst_n[i] > lst_n[j]:
#                 lst_n[i], lst_n[j] = lst_n[j], lst_n[i]
#
#     print('#{}'.format(tc+1), end='')
#     for idx in range(N):
#         print(' {}'.format(lst_n[idx]), end='')
#     print('')

#########################################################
# ladder1

# for tc in range(1, 11):
#     N = int(input())
#     ldr_lst = [list(map(int, input().split())) for _ in range(100)]
#
#     for i in range(100):
#         if ldr_lst[-1][i] == 2:
#             st_c = i
#
#     result = 0
#     for r in range(98, 0, -1):
#         if st_c-1 > 0 and ldr_lst[r][st_c-1] == 1:
#             st_c -= 1
#             while ldr_lst[r-1][st_c] == 0:
#                 st_c -= 1
#         elif st_c + 1 < 100 and ldr_lst[r][st_c+1] == 1:
#             st_c += 1
#             while ldr_lst[r-1][st_c] == 0:
#                 st_c += 1
#
#         result = st_c
#
#     print('#{} {}'.format(tc, result))