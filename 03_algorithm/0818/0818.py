#########################################################
# 0818
#########################################################
# 스택연습 -1

# lst = [3, 7, 5, 9, 2, 8]
# st = []
#
# for i in range(6):
#     st.append(lst[i])
#     print(lst[i], end=' ')
#
# for j in range(6):
#     print(st.pop(), end=' ')
#########################################################
# 스택연습 -1 - 교수님 풀이

# lst = [3,7,5,9,2,8]
# tong = []
#
# for i in range(len(lst)):
#     print(lst[i], end = ' ')
#     tong.append(lst[i])
#
# while tong :
#     ret = tong.pop()
#     print(ret , end = ' ')

#########################################################
# 스택연습

# test_case = int(input())
#
# for tc in range(test_case):
#     N = int(input())
#     lst_n = [input().rstrip() for _ in range(N)]
#     tong = []
#     print('#{}'.format(tc+1))
#     for idx in range(N):
#         if lst_n[idx][0] == 'i':
#             tmp, num = lst_n[idx].split()
#             tong.append(num)
#         elif lst_n[idx] == 'c':
#             print(len(tong))
#         elif lst_n[idx] == 'o':
#             if len(tong) > 0:
#                 print(tong.pop())
#             else:
#                 print('empty')

#########################################################
# 스택연습 - 교수님 풀이

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     tong = []
#     print("#{}".format(tc))
#     for i in range(N):
#         temp = input().rstrip().split()
#         if temp[0] == 'i':
#             # 스택에 insert
#             tong.append(temp[1])
#         elif temp[0] == 'c':
#             # 스택사이즈 출력
#             print(len(tong))
#         elif temp[0] == 'o':
#             # 스택에서 pop
#             if not tong :
#                 print('empty')
#             else :
#                 print(tong.pop())


#########################################################
# 재귀호출
# def abc(n) :
#     if n == 3:
#         return
#     print(n, end=' ')
#     abc(n + 1)
#     print(n, end=' ')
#
#     return # abc가 종료/호출해준 위치로 복귀
#
# abc(0)

#########################################################
# 파스칼 삼각형

# test_case = int(input())
#
# for tc in range(test_case):
#     num = int(input())
#     for idx in range(num):
