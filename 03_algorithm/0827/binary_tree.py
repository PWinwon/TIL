######################################################
# 이진 트리 순회 연습 - 하드 코딩

# def dfs(now) :
#     if now == 0 :
#         return
#     # print(now, end=' ') # 전위 순회 (preorder)
#     preorder.append(now)
#     dfs(left[now]) # 왼쪽
#     # print(now, end=' ') # 중위 순회 (inorder)
#     inorder.append(now)
#     dfs(right[now]) # 오른쪽
#     # print(now, end=' ') # 후위 순회 (postorder)
#     postorder.append(now)
#     return
#
# left = [0 for _ in range(11)]
# right = [0 for _ in range(11)]
#
# root = 1
# left[1] = 3
# right[1] = 5
# left[3] = 2
# right[3] = 6
# left[5] = 7
# right[5] = 8
# left[7] = 9
# left[9] = 10
# right[8] = 4
#
# preorder = []
# postorder = []
# inorder = []
#
#
#
# dfs(root)
#
# print(' '.join(map(str, preorder)))
# print(' '.join(map(str, inorder)))
# print(' '.join(map(str, postorder)))

############################################################
# 교수님 풀이

# def dfs(now) :
#     if now == 0 :
#         return
#     preorder.append(now)
#     dfs(left[now]) # 왼쪽
#     inorder.append(now)
#     dfs(right[now]) # 오른쪽
#     postorder.append(now)
#     return
#
# left = [0 for _ in range(11)]
# right = [0 for _ in range(11)]
#
# root = 1
# left[1] = 3
# right[1] = 5
# left[3] = 2
# right[3] = 6
# left[5] = 7
# right[5] = 8
# left[7] = 9
# left[9] = 10
# right[8] = 4
#
# preorder = [] # 저장하기
# postorder = []
# inorder  = []
# dfs(root)
#
# print(*preorder)
# print(*postorder)
# print(*inorder)


######################################################
# 이진 트리 순회 연습

'''
1 3 1 5 3 2 3 6 5 7 5 8 7 9 8 4 9 10
'''


# def dfs(n):
#     if n > 31 or lst_v[n] == 0:
#         return
#     preorder.append(lst_v[n])
#     dfs(n*2)
#     inorder.append(lst_v[n])
#     dfs(n*2 + 1)
#     postorder.append(lst_v[n])
#     return
#
# v = 10
#
# lst_v = [0 for _ in range(32)]
# lst_v[1] = 1
# lst_v[2] = 3
# lst_v[3] = 5
# lst_v[4] = 2
# lst_v[5] = 6
# lst_v[6] = 7
# lst_v[12] = 9
# lst_v[15] = 4
# lst_v[24] = 10
#
#
# preorder = []
# inorder = []
# postorder = []
# dfs(1)

# print(preorder)
# print(postorder)
# print(inorder)

######################################################
# 이진 트리 순회 연습 - 교수님 풀이

# def dfs(now):
#     if now > 31 or tree[now] == 0: return
#     preorder.append(tree[now])
#     dfs(now * 2) # left
#     inorder.append(tree[now])
#     dfs(now*2 + 1) # right
#     postorder.append(tree[now])
#     return
#
#
# tree = [0 for _ in range(32)]
# tree[1] = 1
# tree[2] = 3
# tree[3] = 5
# tree[4] = 2
# tree[5] = 6
# tree[6] = 7
# tree[7] = 8
# tree[12] = 9
# tree[15] = 4
# tree[24] = 10
#
# preorder = []
# inorder = []
# postorder = []
# dfs(1)
# print(*preorder)
# print(*inorder)
# print(*postorder)

