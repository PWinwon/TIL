## 2차원 리스트 2중 for 문 탐색
# lst = [
#     #0 1 2 3
#     [3,2,1,5], # 0 번 라인
#     [1,2,3,4], # 1 번 라인
#     [5,4,3,2]  # 2 번 라인
# ]
#
# # [0][1] <-> [2][2]
# lst[0][1],lst[2][2] = lst[2][2], lst[0][1] # swap
#
# for line in [0,1,2] :
#     lst[line]
#     for x in [0,1,2,3]:
#         print(lst[line][x], end = ' ')
#     print()

################################################################
# lst = [1차원 리스트 먼저 만들고 얘를 몇개 만들지 ]

# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)] # N개의 1차원 리스트가 만들어짐

################################################################

# MAP = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(MAP[1-1][1+0], end = ' ')
# print(MAP[1+1][1+0], end = ' ')
# print(MAP[1+0][1-1], end = ' ')
# print(MAP[1+0][1+1], end = ' ')
# print('')
#
# y = 1
# x = 1
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# for t in range(4):
#     ny = y + dy[t]
#     nx = x + dx[t]
#     if ny < 0 or nx < 0 or ny >= 3 or nx >= 3:  # 범위 바깥으로 나가면 continue -> 다음 반복 진행
#         continue
#     print(MAP[ny][nx], end = ' ')


################################################################
# 델타 검색
# for tc in range(1, 11):
#     N = int(input())
#     lst_n = [list(map(int, input().split())) for _ in range(N)]
#
#     dy = [-1, 1, 0, 0]
#     dx = [0, 0, -1, 1]
#     result = 0
#
#     for y in range(N):
#         for x in range(N):
#             for t in range(4):
#                 ny = y + dy[t]
#                 nx = x + dx[t]
#                 if ny < 0 or nx < 0 or ny >= N or nx >= N:
#                     continue
#                 if lst_n[ny][nx] > lst_n[y][x]:
#                     result += lst_n[ny][nx] - lst_n[y][x]
#                 else:
#                     result += lst_n[y][x] - lst_n[ny][nx]
#     print('#{} {}'.format(tc, result))

################################################################
#
# bit = [
#     [0,0,0], #0
#     [0,0,1], #1
#     [0,1,0], #2
#     [0,1,1], #3
#     [1,0,0], #4
#     [1,0,1], #5
#     [1,1,0], #6
#     [1,1,1], #7
# ]
#
# lst = [10,3,9]
#
# # 부분집합 출력하기
#
# for k in range(8):
#     for i in range(3):
#         if bit[k][i] == 1:
#             print(lst[i],end = ' ') # bit 비교했을때 lst[i]에 1이 있으면 출력
#     print()

################################################################
# 부분집합 합

# for tc in range(1,11):
#     N = int(input())
#     lst_n = list(map(int, input().split()))
#     result = 0
#     for i in range(1<<N):
#         total = 0
#         for j in range(N+1):
#             if i & (1<<j):
#                 total += lst_n[j]
#         if total == 0:
#             result += 1
#     print('#{} {}'.format(tc, result))


##################################################################
# 선택정렬
# lst = [3, 2, 9, 5, 8, 6, 1]
# N = 7
# for y in range(N):  # 0 ~ 6 기준
#     for x in range(y, N):  # 기준 ~ 오른쪽 끝까지
#         if lst[y] > lst[x]:
#             lst[y], lst[x] = lst[x], lst[y]
#
#     # 기준에 작은 값을 위치시킴
#
# for i in range(N):
#     print(lst[i], end=' ')

##################################################################
#

# N = int(input())
# lst = [N + (2 * i)  for i in range(10)]
# print(lst)

##################################################################
# 달팽이 숫자

# dir_x = [1, 0, -1, 0]
# dir_y = [0, 1, 0, -1]
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     max_n = N * N
#     cnt = 1
#     idx_x = 0
#     idx_y = 1
#     idx_d = 0
#     dalpang_lst = [[-1 for _ in range(N + 2)] for _ in range( N + 2)]
#     for y in range(1, N + 1):
#         for x in range(1, N + 1):
#             dalpang_lst[y][x] = 0
#     while cnt <= max_n:
#         idx_x += dir_x[idx_d]
#         idx_y += dir_y[idx_d]
#         if dalpang_lst[idx_y][idx_x] == 0:
#             dalpang_lst[idx_y][idx_x] = cnt
#             cnt += 1
#         else:
#             idx_x -= dir_x[idx_d]
#             idx_y -= dir_y[idx_d]
#             idx_d = (idx_d + 1) % 4
#     print('#{}'.format(tc+1))
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             print(dalpang_lst[i][j], end=' ')
#         print('')

##################################################################
# sum

for tc in range(10):
    T = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    result = []
    max_val = 0
    cross_1 = 0
    cross_2 = 0
    for y in range(100):
        garo_sum = 0
        sero_sum = 0
        for x in range(100):
            garo_sum += lst[y][x]
            sero_sum += lst[x][y]
            if x == y:
                cross_1 += lst[x][y]
            if x + y == 99:
                cross_2 += lst[x][y]
        result.append(garo_sum)
        result.append(sero_sum)
    result.append(cross_1)
    result.append(cross_2)

    for idx in range(len(result)):
        if max_val < result[idx]:
            max_val = result[idx]
    print('#{} {}'.format(T, max_val))