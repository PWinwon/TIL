for t in range(10):
    v, e = map(int, input().split())
    list_n = list(map(int, input().split()))
    e_start = []
    e_end = []
    # 입력받은 값(간선의 방향)에 대해 시작점과 도착점을 나누어 각각의 리스트에 저장
    for idx_e in range(0, 2*e , 2):
        e_start.append(list_n[idx_e])
        e_end.append(list_n[idx_e+1])
    
    result = []
    # 반복문을 통해 result와 e_end에 없으면 >> 자신을 향하는 간선이 없다.
    # 즉 작업의 우선순위에서 먼저 작업이 이루어져야한다
    # 만족하면 그 값을 result에 append 함
    while len(result) < v:
        for i in range(1, v+1):
            if i not in result and i not in e_end:
                result.append(i)
                idx = 0
                # 우선 순위 높은 i 가 result에 append 되었다 >> i 작업이 실행되었다
                # >> i로 시작하는 노드를 지워 다음 작업이 이루어 질 수 있도록 한다.
                while idx < len(e_start):
                    if e_start[idx] == i:
                        e_start.pop(idx)
                        e_end.pop(idx)
                    # pop을 실행해 out of range 가 생기므로 이를 고려해 idx 조절
                    else:
                        idx += 1
    # 값 조절
    print(f'#{t+1}', end = '')
    for j in range(v):
        print(f' {result[j]}', end = '')
    print('')
