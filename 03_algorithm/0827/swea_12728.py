def bfs(now):
    if now == 0:
        return
    result.append(now)
    bfs(left[now])
    bfs(right[now])
    return

test_case = int(input())

for tc in range(test_case):
    v = int(input())
    lst_v = [list(map(int, input().split())) for i in range(v-1)]
    left = [0] * (v+1)
    right = [0] * (v+1)
    result = []
    for i in range(v-1):
        if left[lst_v[i][0]] == 0:
            left[lst_v[i][0]] = lst_v[i][1]
        else:
            right[lst_v[i][0]] = lst_v[i][1]

    bfs(1)
    print('#{} {}'.format(tc+1, ' '.join(map(str, result))))

############################################################################
# 교수님 풀이

# def dfs(now):
#     if now == 0 : return
#     preorder.append(now)
#     dfs(left[now])
#     dfs(right[now])
#     return
#
# T = int(input())
#
# for tc in range(1,T+1):
#     K = int(input())
#     left = [0 for _ in range(20)]
#     right = [0 for _ in range(20)]
#
#     for _ in range(K-1) :
#         parent, child = map(int,input().split())
#         if left[parent] == 0:
#             left[parent] = child
#         else :
#             right[parent] = child
#
#     preorder = []
#     dfs(1)
#
#     print("#{}".format(tc),end = ' ')
#     print(*preorder)