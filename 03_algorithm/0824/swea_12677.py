def cardgame(arr):
    if len(arr) <= 2:
        if len(arr) == 1:
            return arr[0]
        else:
            if lst[arr[0]] == lst[arr[1]]:
                return arr[0]
            else:
                res = who_win(arr[0], arr[1])
                return res
    else:
        idx1 = cardgame(arr[:(len(arr)+1)//2])
        idx2 = cardgame(arr[(len(arr)+1)//2:])
        return cardgame([idx1, idx2])


def who_win(a, b):
    if lst[a] == 1:
        if lst[b] == 2:
            return b
        else:
            return a
    elif lst[a] == 2:
        if lst[b] == 3:
            return b
        else:
            return a
    else:
        if lst[b] == 1:
            return b
        else:
            return a


test_case = int(input())

for tc in range(test_case):
    N = int(input())
    lst = list(map(int, input().split()))
    lst_num = [i for i in range(N)]
    de = -1
    result = cardgame(lst_num)
    print('#{} {}'.format(tc+1, result + 1))

###########################################################
# 토너먼트 카드 게임 - 교수님 풀이

# def winner(a,b):
#     if card[a] == card[b] : return a
#     if (card[a] == 1 and card[b] == 3) or \
#             (card[a] == 2 and card[b] == 1) or \
#             (card[a] == 3 and card[b] == 2) :
#         return a
#     else :
#         return b
#
#
# def dfs(s,e):
#     if s == e :
#         return s
#     mid = (s+e)//2
#     a = dfs(s,mid) # 왼쪽
#     b = dfs(mid+1,e) # 오른쪽
#     ret = winner(a,b)
#     return ret
#
# card = [-1]
# N = int(input())
# card += list(map(int,input().split()))
# ret = dfs(1,N)
# print(ret)