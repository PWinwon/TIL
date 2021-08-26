from collections import deque


test_case = int(input())

for tc in range(test_case):
    fire, pizza = map(int, input().split())
    lst_pz = list(map(int, input().split()))
    que = deque()
    que_idx = deque()
    cnt = 0
    for i in range(fire):
        que.append(lst_pz[i])
        que_idx.append(i)
        cnt += 1

    while que:
        temp = que.popleft()
        temp = temp // 2
        idx = que_idx.popleft()
        if temp == 0 and cnt < pizza:
            que.append(lst_pz[cnt-1])
            que_idx.append(cnt)
            cnt += 1
        elif temp > 0:
            que.append(temp)
            que_idx.append(idx)

        if len(que) == 1:
            break
    print('#{} {}'.format(tc+1, que_idx[0]))



#############################################################################################
# 교수님 풀이

# import sys
# sys.stdin = open("text.txt","r")
#
# from collections import deque
#
# T = int(input())
#
# for tc in range(1,T+1) :
#     N,M = map(int, input().split())
#     cheese = [-1]
#     cheese += list(map(int,input().split()))
#     oven = deque(range(1,N+1)) # oven에 1번피자 ~ N번피자
#
#     num = N+1
#     while len(oven) > 1 :
#         pizza_num = oven[0]
#         cheese[pizza_num] //= 2
#         if cheese[pizza_num] == 0 :
#             oven.popleft()
#             if num <= M:
#                 oven.append(num)
#                 num += 1
#         else :
#             tmp = oven.popleft()
#             oven.append(tmp)
#
#     print(oven[0])