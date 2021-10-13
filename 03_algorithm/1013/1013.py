########################################################
# 최종 부모 찾기

'''
# 교수님 풀이
def Find(ch) : # 최종 부모를 찾는다.
    if parent[ch] == ch:
        return ch # 최종부모를 return
    ret = Find(parent[ch])
    # 나중에 경로 압축 (효율적인 연산)추가 예정
    return ret
'''

# def my_find(s):
#     key = s
#     while True:
#         if key == parent[key]:
#             break
#         key = parent[key]
#     return key
#
#
# parent = dict()
#
# for ch in range(ord('A'), ord('Z') + 1):
#     parent[chr(ch)] = chr(ch)
#
# print(parent)
#
# parent['E'] = 'D'
# parent['D'] = 'C'
# parent['C'] = 'B'
# parent['B'] = 'A'
#
# print(my_find('E'))
# print(my_find('D'))
# print(my_find('B'))
# print(my_find('A'))


################################################
# union find 기본 코드 - 교수님 풀이

# parent = dict()
#
# # make - set
# for ch in range(ord('A') , ord('Z') + 1):
#     parent[chr(ch)] = chr(ch)
#
#
# def Union(a,b): # a의그룹 <- b그룹
#     pa = Find(a) # a 의 그룹 대표자(최종 부모) 를 찾는다.
#     pb = Find(b) # b 의 그룹 대표자(최종 부모) 를 찾는다.
#     if pa != pb :
#         parent[pb] = pa
#
# def Find(ch) : # 최종 부모를 찾는다.
#     if parent[ch] == ch:
#         return ch # 최종부모를 return
#     ret = Find(parent[ch])
#     # 나중에 경로 압축 (효율적인 연산)추가 예정
#     return ret
#
#
# Union('A', 'B')
# Union('C', 'D')
# Union('D', 'B')
# Union('B', 'D') # 이미 같은 그룹

################################################################
# 경로 압축 버전
# parent = dict()
#
# # make - set init
# for ch in range(ord('A') , ord('Z') + 1):
#     parent[chr(ch)] = chr(ch)
#
#
# def Union(a,b): # a의그룹 <- b그룹
#     pa = Find(a) # a 의 그룹 대표자(최종 부모) 를 찾는다.
#     pb = Find(b) # b 의 그룹 대표자(최종 부모) 를 찾는다.
#     if pa != pb :
#         parent[pb] = pa
#
# def Find(ch) : # 최종 부모를 찾는다.
#     if parent[ch] == ch:
#         return ch # 최종부모를 return
#     ret = Find(parent[ch])
#     parent[ch] = ret # 경로압축
#     return ret
#
#
# parent['E'] = 'D'
# parent['D'] = 'C'
# parent['C'] = 'B'
# parent['B'] = 'A'
#
#
#
# # Union('A', 'B')
# # Union('C', 'D')
# # Union('D', 'B')
# # Union('B', 'D') # 이미 같은 그룹