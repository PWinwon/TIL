test_case = int(input())

for tc in range(test_case):
    N, M = map(int, input().split())
    lst = list(map(int, input().split())) + [0] * 2000
    front = 0
    rear = N
    temp = 0
    for _ in range(M):
        temp = lst[front]
        lst[rear] = temp
        front += 1
        rear += 1
    print('#{} {}'.format(tc+1, lst[front]))

####################################################################
# 교수님 풀이

# T = int(input())
#
# for tc in range(1,T+1):
#     N,M = map(int, input().split()) # 정수 개수, 회전수
#     temp = list(map(int,input().split()))
#     queue = [0 for _ in range(2000)]
#     front = 0
#     rear = 0
#     for i in range(len(temp)):
#         queue[rear] = temp[i]
#         rear += 1
#     de = -1
#     i = 0
#     while i < M: # 총 M 번 회전
#
#         # peek + deque
#         a = queue[front]
#         front += 1
#         # enque
#         queue[rear] = a
#         rear += 1
#         i += 1
#
#     print("#{} {}".format(tc, queue[front]))