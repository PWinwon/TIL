# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     boxes = list(map(int, input().split()))
#     trucks = list(map(int, input().split()))
#     boxes.sort(reverse=True)
#     used = [0] * N
#     result = 0
#     for t in range(M):
#         for b in range(N):
#             if trucks[t] >= boxes[b] and used[b] == 0:
#                 used[b] = 1
#                 result += boxes[b]
#                 break
#     print('#{} {}'.format(tc, result))

####################################################
# 교수님 풀이

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    load = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    de = -1
    # 트럭 내림차순으로 정렬하기
    truck.sort(reverse=True)
    used = [0] * N
    ans = 0
    for t in range(len(truck)):
        # 제일 큰거 찾기
        idx = -1
        max_load = -int(21e8)
        for i in range(len(load)):
            if used[i] == 1: continue
            if max_load < load[i] and truck[t] >= load[i]:
                idx = i
                max_load = load[i]

        # truck[t] 에 실을까?
        if idx != -1:
            used[idx] = 1
            ans += load[idx]

    print("#{} {}".format(tc, ans))