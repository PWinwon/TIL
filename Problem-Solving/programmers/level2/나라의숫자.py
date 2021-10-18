order = ['1', '2', '4']
def solution(n):
    answer = ''
    while n:
        answer += order[n%3 -1]
        n = (n-1) // 3
    answer = answer[::-1]
    return answer