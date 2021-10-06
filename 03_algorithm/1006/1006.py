#######################################################
# merge sort 연습

# def merge_sort(s, e):
#     if s == e:
#         return [lst[s]]
#     mid = (s + e) // 2
#     left = merge_sort(s, mid)
#     right = merge_sort(mid+1, e)
#     l_idx = 0
#     r_idx = 0
#     l_len = len(left)
#     r_len = len(right)
#     temp = [0] * (l_len + r_len)
#     idx = 0
#     while idx < len(temp):
#         if l_idx >= l_len:
#             temp[idx] = right[r_idx]
#             idx += 1
#             r_idx += 1
#         elif r_idx >= r_len:
#             temp[idx] = left[l_idx]
#             idx += 1
#             l_idx += 1
#         elif left[l_idx] > right[r_idx]:
#             temp[idx] = right[r_idx]
#             idx += 1
#             r_idx += 1
#         else:
#             temp[idx] = left[l_idx]
#             idx += 1
#             l_idx += 1
#     return temp
#
#
# lst = [4, 7, 2, 1, 8, 5]
# result = merge_sort(0, 5)
# print(result)

#################################################################
# 정렬된 두 배열 merge - 교수님풀이

# lst = [4,7,2,1,8,5]
#
# def merge_sort(s, e ):
#     if s == e :
#         return
#     mid = (s + e ) // 2
#     merge_sort(s,mid) # 왼쪽 부분 정렬
#     merge_sort(mid+1, e) # 오른쪽 부분 정렬
#
#     # merge 해주기
#     # left [s~mid]     [s : mid + 1]    / right [mid+1 ~ e]     [mid + 1 : e + 1]
#     a = s
#     b = mid+1
#     res = []
#     while a <= mid and b <= e :
#         if lst[a] <= lst[b] :
#             res.append(lst[a])
#             a += 1
#         elif lst[b] < lst[a] :
#             res.append(lst[b])
#             b += 1
#     while a <= mid :
#         res.append(lst[a])
#         a += 1
#     while b <= e :
#         res.append(lst[b])
#         b += 1
#
#     # res -> lst 에 복사
#     t = 0
#     for i in range(s, e + 1) : # [s ~ e]
#         lst[i] = res[t]
#         t += 1
#
#     print(lst[s:e + 1])
#
# merge_sort(0,5) # [s ~ e]


###################################################################
# Quick sort 구현해보기

'''
11 45 23 81 28 34

11 45 22 81 23 34 99 22 17 8

1 1 1 1 1 0 0 0 0 0
'''


# def quick_sort(s, e):
#     pivot = lst[s]
#     sml = s
#     big = e
#     while
#
# T = int(input())
#
# for tc in range(T):
#     lst = list(map(int, input().split()))

###################################################################
# Binary search 구현해보기 - while

# lst = [1, 2, 5, 7, 15, 20, 300]
# s = 0
# e = 6
# find = 5
# result = -1
# while True:
#     mid = (s+e) // 2
#     if s >= e and lst[s] != find:
#         break
#     elif lst[mid] == find:
#         result = mid
#         break
#     elif lst[mid] > find:
#         e = mid-1
#     else:
#         s = mid+1
# if result < 0:
#     print('NOT FOUND {}'.format(find))
# else:
#     print('FIND {}`s index : {}'.format(find, result))

###################################################################
# Binary search 구현해보기 - 재귀

# def binary_search(s, e, f):
#     global ret, chk
#     if chk:
#         return
#     if s >= e and lst[s] != f:
#         ret = -1
#         chk = True
#         return
#     mid = (s+e) // 2
#     if lst[mid] == f:
#         ret = mid
#         chk = True
#         return
#     elif lst[mid] > f:
#         binary_search(s, mid-1, f)
#     else:
#         binary_search(mid+1, s, f)
#     return
#
#
# lst = [1, 2, 5, 7, 15, 20, 300]
# chk = False
# ret = -1
# binary_search(0, 6, 5)
# print(ret)


###################################################################
# Binary search 구현해보기 - while - 교수님 풀이

# lst = [1,2,5,7,15,20,300] # 정렬된 데이터
#
# def binary_search(lst, target) :
#     s = 0
#     e = len(lst) - 1
#
#     while s <= e :
#         mid = (s + e) // 2
#
#         if target == lst[mid] :
#             print("찾았다")
#             return mid
#         elif target < lst[mid] : # s   target... mid   e
#             e = mid - 1
#         elif lst[mid] < target : # s   mid...target    e
#             s = mid + 1
#
#     return -1# 못찾은 경우
#
# ret = binary_search(lst, 5)
# if ret == -1 :
#     print("못찾음")
# else :
#     print("{} : {}index 에 있다".format(lst[ret], ret))

###################################################################
# Binary search 구현해보기 - 재귀 - 교수님풀이

# lst = [1,2,5,7,15,20,300] # 정렬된 데이터
#
# ans = 0
# def binary_search(s, e, target) :
#     global ans
#     if s > e :
#         ans = - 1
#         return
#     mid = (s + e) // 2
#     if lst[mid] == target :
#         ans = mid
#         return
#     elif target < lst[mid] : # s target mid e
#         binary_search(s,mid - 1)
#     elif lst[mid] < target : # s mid target e
#         binary_search(mid + 1, e)
#
#     return


##############################################################
# string 입력 -> '#' or '_' 로 채워진
# ex ) '#######____________'
# 최종 # 이 몇번째 인덱스 까지 채워져 있을까?
'''
#########_____
-> 8
###____________
-> 2
##########__
->9
___________________
-> -1
##############
-> 14 
'''

# charge = '#############_'
# s = 0
# e = 14
# result = -1
# res = -1
# while s <= e:
#     mid = (s+e) // 2
#     if mid + 1 >= len(charge):
#         result = len(charge)
#         break
#     if charge[mid] == '#' and charge[mid+1] == '_':
#         result = mid
#         break
#     if charge[mid] == '#':
#         s = mid + 1
#     else:
#         e = mid - 1
# print(result)

###############################################################
# string 입력 -> '#' or '_' 로 채워진
# ex ) '#######____________'
# 최종 # 이 몇번째 인덱스 까지 채워져 있을까? - 교수님 풀이

# lst = input() # 최대 인덱스 찾기
#
# s = 0
# e = len(lst) -1
# ans = -1
# while s <= e :
#     mid = (s + e) // 2
#
#     if lst[mid] == '#':   #      s   #(mid)->    e
#         ans = mid
#         s = mid + 1
#     else :  #    s    <-_(mid)   e
#         e = mid - 1
#
# print(ans)

##############################################################
# 트리 순회

