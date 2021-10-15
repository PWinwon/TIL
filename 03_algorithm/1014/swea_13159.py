def Find(n):
    if parents[n] == n:
        return n
    ret = Find(parents[n])
    parents[n] = ret
    return ret


def Union(a, b):
    global result
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        parents[pb] = pa
        result -= 1
    return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))
    parents = [i for i in range(N+1)]
    result = N
    for m in range(M):
        a = pairs[m*2]
        b = pairs[m*2+1]
        Union(a, b)
    print('#{} {}'.format(tc, result))


# 교수님 풀이

# T = int(input())
#
# def Find(a) :
#     if a == parent[a] :
#         return a
#     ret = Find(parent[a])
#     parent[a] = ret # 경로 압축  (최종부모와 직접연결)
#     return ret
#
# def Union(a,b):
#     pa = Find(a) # a 가 속한그룹 대표자 찾기
#     pb = Find(b) # b ""
#     if pa != pb :
#         parent[pb] = pa
#     return
#
# for tc in range(1, T + 1) :
#     N , M = map(int , input().split()) # 1 ~ N 번 존재 / M 개 쌍 입력
#     lst = list(map(int ,input().split()))
#     group_cnt = 0
#     # init {1},{2},{3},....{N}
#     parent = [i for i in range(N+1)]
#     group_cnt = N # 처음에는 N개의 그룹
#
#     for i in range(0,2*M,2):
#         a,b = lst[i], lst[i+1]
#         if Find(a) != Find(b) : # 최종 부모가 다르다 == 다른그룹일때
#             group_cnt -= 1 # 전체그룹수 1감소
#         Union(a,b)
#
#     print("#{} {}".format(tc, group_cnt))
