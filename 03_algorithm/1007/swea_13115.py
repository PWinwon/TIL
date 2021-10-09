# def binary_search_chk(s, e, f, chk):
#     global res
#     if s > e:
#         return
#     mid = (s + e) // 2
#     if f == lst_n[mid]:
#         res += 1
#         return
#     elif f < lst_n[mid] and (chk == 'r' or chk == 'first'):
#         binary_search_chk(s, mid-1, f, 'l')
#     elif f > lst_n[mid] and (chk == 'l' or chk == 'first'):
#         binary_search_chk(mid+1, e, f, 'r')
#     return
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     lst_n = list(map(int, input().split()))
#     lst_m = list(map(int, input().split()))
#     lst_n.sort()
#     res = 0
#     for m in lst_m:
#         binary_search_chk(0, N-1, m, 'first')
#     print('#{} {}'.format(tc, res))

#############################################################
# 교수님 풀이

# def binary_search(s,e, target):
#     flag = 0 # 'left' ,'right' 이전상태
#     while s <= e :
#         mid = (s + e) // 2
#         if A[mid] == target :
#             return True
#         elif target < A[mid] :
#             if flag == 0 : flag = 'right'
#             elif flag == 'right' : return False
#             flag = 'right'
#             e = mid - 1 # s  mid target  e   right 구간선택함
#         elif A[mid] < target :
#             if flag == 0 : flag = 'left'
#             elif flag == 'left' : return False
#             flag = 'left'
#             s = mid + 1 # s target  mid   e    left 구간선택
#
#     return False
#
#
# T = int(input())
#
# for tc in range(1, T + 1) :
#     N,M = map(int, input().split()) # N : A의 크기 , M : B 의 크기
#     A = list(map(int ,input().split()))
#     B = list(map(int ,input().split()))
#     A.sort()
#     cnt = 0
#     for i in range(len(B)):
#         target = B[i]
#         ret = binary_search(0,len(A)-1, target) # 존재하고 + 번갈아가면서 탐색되는지
#         if ret == True:
#             cnt += 1
#     print("#{} {}".format(tc, cnt))