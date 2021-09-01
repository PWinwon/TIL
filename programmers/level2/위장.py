def solution(clothes):
    answer = 1
    hash1 = {}
    for cloth in clothes:
        if cloth[1] in hash1:
            hash1[cloth[1]] += 1
        else:
            hash1[cloth[1]] = 1
    for k, v in hash1.items():
        answer *= v+1
    
    return answer-1