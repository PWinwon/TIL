# 교수님 풀이

def Union(a,b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb : # 다른 그룹이면
        parent[pb] = pa
    return

def Find(a):
    if parent[a] == a : return a

    ret = Find(parent[a])
    parent[a] = ret #경로압축(나의 부모가 최종부모다)
    return ret

N , M = map(int ,input().split()) # N : 초기 집합의 개수 0 ~ N // M : 연산 개수

parent = [ i for i in range(N + 1)] # init     // parent[a] = a의 부모가 저장되어있다.
ans = [] # YES\n , NO\n
for _ in range(M) :
    cmd,a,b = map(int ,input().split())
    if cmd == 0 :
        Union(a,b) #
    elif cmd == 1 :
        pa = Find(a) # 최종 부모 (그룹 대표 찾기)
        pb = Find(b) # 최종 부모 (그룹 대표 찾기)
        if pa != pb :
            ans.append("NO\n") # 다른 그룹
        else :
            ans.append("YES\n") # 같은 그룹

print("{}".format(''.join(ans)))