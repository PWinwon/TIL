def solution(citations):
    answer = 0
    citations.sort()
    print(citations)
    val = 0
    while True:
        for c in range(len(citations)):
            if citations[c] >= val and len(citations) - c >= val:
                answer = val
                break
        else:
            return answer
        val += 1