T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    idx = (1 << N) - 1
    if M & idx == idx:
        print('#{} ON'.format(tc+1))
    else:
        print('#{} OFF'.format(tc + 1))


######################################################
# 교수님 풀이

# T = int(input())
#
# for tc in range(1, T+ 1):
#     N,M = map(int, input().split())
#
#     new_M = M & ((1 << N) -1)
#     de = -1
#     if (1 << N) - 1 == new_M :
#         print("#{} ON".format(tc))
#     else :
#         print("#{} OFF".format(tc))