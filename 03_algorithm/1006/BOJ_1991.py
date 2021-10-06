import sys

def my_func(now):
    global result1, result2, result3
    result1 += now
    if my_dict[now][0] != '.':
        my_func(my_dict[now][0])
    result2 += now
    if my_dict[now][1] != '.':
        my_func(my_dict[now][1])
    result3 += now
    return


N = int(sys.stdin.readline())
lst = [list(sys.stdin.readline().split()) for _ in range(N)]
my_dict = {}
for i in range(N):
    my_dict[lst[i][0]] = lst[i][1:]
result1 = ''
result2 = ''
result3 = ''
my_func('A')
print(result1)
print(result2)
print(result3)


###########################################
# 교수님 풀이

# tree = dict()
#
# N = int(input())
# for _ in range(N) :
#     a,b,c = input().split()
#     tree[a] = [b,c]
#
# de = - 1
# preorder = []
# inorder = []
# postorder = []
#
# def dfs(now) :
#     if now == '.' : return
#
#     preorder.append(now)
#     dfs(tree[now][0]) # left
#     inorder.append(now)
#     dfs(tree[now][1]) # right
#     postorder.append(now)
#
#     return
#
# dfs('A')
# print(''.join(preorder))
# print(''.join(inorder))
# print(''.join(postorder))