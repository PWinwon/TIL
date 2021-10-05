##############################################################
# 클래스 인스턴스를 기준으로 정렬하기

# class abc:
#     def __init__(self, h, w):
#         self.height = h
#         self.weight = w
#
#
# lst = [abc(180, 67), abc(170, 55), abc(180, 65), abc(180, 55), abc(165, 55), abc(170, 40)]
#
# lst.sort(key=lambda x: (-x.height, x.weight))
# print(lst)


##################################################################
# 클래스 인스턴스를 기준으로 정렬하기 - 교수님 풀이

# class abc :
#     def __init__(self, h , w):
#         self.height = h
#         self.weight = w
#
# def cmp(abc_var) :
#     return (-abc_var.height, abc_var.weight)
# lst = [abc(180, 67), abc(170, 55), abc(180, 65), abc(180, 55), abc(165, 55), abc(170,40)]
# de = -1
# lst.sort(key = cmp)
# de = - 1
# for i in range(len(lst)):
#     print(lst[i].height , lst[i].weight, end = ',')
#
# print()
#
# def cmp2(tup):
#     return (-ord(tup[1]),tup[0])
# lst2 = [(1,'a'), (2,'b'), (1,'b')]
# lst2.sort(key = cmp2)
# print(lst2)