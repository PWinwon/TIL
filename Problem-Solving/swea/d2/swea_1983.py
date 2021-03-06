T = int(input())
soc = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(T):
    N, K = map(int, input().split())
    score_list = []
    result = []
    for n in range(N):
        a, b, c, = map(int, input().split())
        score_list.append(a*0.35 + b*0.45 + c*0.2)
    
    for score in score_list:
        rank_score = 0
        for sc in score_list:
            if score < sc:
                rank_score += 1
        result.append(rank_score)
    
    rank = result[K-1]
    idx = int(N // 10)
    rank = rank // idx
    
    print(f'#{i+1} {soc[rank]}')

