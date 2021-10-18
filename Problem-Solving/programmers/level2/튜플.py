def solution(s):
    s = s.replace('{', '').replace('}', '')
    s = list(map(int, s.split(',')))
    idxs = set(s)
    answer = [0] * len(idxs)
    for idx in idxs:
        answer[s.count(idx)-1] = idx
    return answer[::-1]