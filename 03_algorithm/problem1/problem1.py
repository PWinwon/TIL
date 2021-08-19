#########################################################
#########################################################
#########################################################
#########################################################
#                    문제 풀이 1
#########################################################
#########################################################
#########################################################
#########################################################
# 백만 장자 프로젝트

# test_case = int(input())
#
# for tc in range(test_case):
#     n = int(input())
#     lst_n = list(map(int, input().split()))
#
#     max_val = 0
#     total = 0
#     for idx in range(n-1, -1, -1):
#         if lst_n[idx] > max_val:
#             max_val = lst_n[idx]
#         else:
#             total += max_val - lst_n[idx]
#     print('#{} {}'.format(tc+1, total))

#########################################################
# 자기 방으로 돌아가기
#
# test_case = int(input())
#
# for tc in range(test_case):
#     n = int(input())
#     lst_n = [list(map(int, input().split())) for _ in range(n)]
#     lst_room = [0] * 200
#     for idx in range(n):
#         if lst_n[idx][0] > lst_n[idx][1]:
#             lst_n[idx][0], lst_n[idx][1] = lst_n[idx][1], lst_n[idx][0]
#         st = (lst_n[idx][0]-1)//2
#         ed = (lst_n[idx][1]-1)//2
#         for move in range(st, ed+1):
#             lst_room[move] += 1
#     max_move = 0
#     for m in range(200):
#         if max_move < lst_room[m]:
#             max_move = lst_room[m]
#     print('#{} {}'.format(tc+1, max_move))

#########################################################
# 쇠막대기 자르기
#
# test_case = int(input())
#
# for tc in range(test_case):
#     slice_str = input()
#     cnt = 0
#     total = 0
#     for slc in range(len(slice_str)):
#         if slice_str[slc] == '(' and slice_str[slc+1] == ')':
#             total += cnt
#         elif slice_str[slc] == '(':
#             cnt += 1
#             total += 1
#         elif slice_str[slc] == ')' and slice_str[slc-1] != '(':
#             cnt -= 1
#     print('#{} {}'.format(tc+1, total))
#########################################################
# 마법사의 사냥
# 좌상 우상 좌하 우하
# def monster_kill(row, col, n, k):
#     dir_r = [-1, -1, 1, 1]
#     dir_c = [-1, 1, -1, 1]
#     total = 0
#     for idx in range(4):
#         idx_r = row
#         idx_c = col
#         cnt = 0
#         while idx_r + dir_r[idx] >= 0 and idx_r + dir_r[idx] < n and idx_c + dir_c[idx] >= 0 and idx_c + dir_c[idx] < n:
#             idx_r += dir_r[idx]
#             idx_c += dir_c[idx]
#             total += field_mon[idx_r][idx_c]
#             cnt += 1
#             if cnt == k:
#                 break
#     return total
#
# for tc in range(1, 6):
#     N = int(input())
#     field_mon = [list(map(int, input().split())) for _ in range(N)]
#     K = int(input())
#
#     result = 0
#     for r in range(N):
#         for c in range(N):
#             cnt = monster_kill(r, c, N, K)
#             if result < cnt:
#                 result = cnt
#     print('#{} {}'.format(tc, result))

#########################################################
# 삼성시의 버스 노선
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N = int(input())
#     lst_bus = [list(map(int, input().split())) for _ in range(N)]
#     lst_bs = [0] * 5000
#     for bus in range(N):
#         for idx in range(lst_bus[bus][0]-1, lst_bus[bus][1]):
#             lst_bs[idx] += 1
#
#     result = '#{}'.format(tc+1)
#     P = int(input())
#     for _ in range(P):
#         C = int(input())
#         result += ' {}'.format(lst_bs[C-1])
#
#     print(result)

#########################################################
# 의석이의 세로로 말해요
#
# test_case = int(input())
#
# for tc in range(test_case):
#     lst_n = [input() for _ in range(5)]
#
#     result = '#{} '.format(tc+1)
#     for r in range(15):
#         for c in range(5):
#             if r < len(lst_n[c]):
#                 result += lst_n[c][r]
#
#     print(result)

#########################################################
# 스도쿠 검증

# def sdoqu_chk(lst):
#     for num in range(1,10):
#         cnt = 0
#         for idx in range(9):
#             if num == lst[idx]:
#                 cnt +=1
#         if cnt > 1:
#             return True
#     return False
#
# test_case = int(input())
#
# for tc in range(test_case):
#     sdoqu = [list(map(int, input().split())) for _ in range(9)]
#
#     result = 1
#     for r in range(9):
#         sero = []
#         if sdoqu_chk(sdoqu[r]):
#             result = 0
#         for c in range(9):
#             sero.append(sdoqu[c][r])
#         if sdoqu_chk(sero):
#             result = 0
#
#     for r in range(0, 9, 3):
#         for c in range(0, 9, 3):
#             sqare = []
#             for r_idx in range(r, r+3):
#                 for c_idx in range(c, c+3):
#                     sqare.append(sdoqu[r_idx][c_idx])
#             if sdoqu_chk(sqare):
#                 result = 0
#
#     print('#{} {}'.format(tc+1, result))


#########################################################
# 숫자 배열 회전

# def rotate_90(lst, n):
#     result = []
#     for r in range(n):
#         row = []
#         for c in range(n-1, -1, -1):
#             row.append(lst[c][r])
#         result.append(row)
#     return result
#
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N = int(input())
#     lst_n = [list( input().split()) for _ in range(N)]
#
#     lst_90 = rotate_90(lst_n, N)
#     lst_180 = rotate_90(lst_90, N)
#     lst_270 = rotate_90(lst_180, N)
#
#
#     print('#{}'.format(tc+1))
#     for r in range(N):
#         print(''.join(lst_90[r]), end=' ')
#         print(''.join(lst_180[r]), end=' ')
#         print(''.join(lst_270[r]))
