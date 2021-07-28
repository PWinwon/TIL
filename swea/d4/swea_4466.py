T = int(input())

for i in range(T):
    # N, K , 그리고 성적들을 입력받아옴
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    #성적들을 내림차순으로 정렬하여 앞쪽부터 K 까지 큰값들을 불러 sum 함수를 이용해 최대성적을 출력
    scores.sort(reverse=True)
    result = sum(scores[0:K])
    print(f'#{i+1} {result}')
