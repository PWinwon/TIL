def solution(s):
    answer = 0
    stack = []
    idx = 0
    sl = len(s)
    while idx < sl:
        if stack:
            if stack[-1] == s[idx]:
                stack.pop()
            else:
                stack.append(s[idx])
        else:
            stack.append(s[idx])
        idx += 1
            
    if stack:
        return answer
    else:
        return 1