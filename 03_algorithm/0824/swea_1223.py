# 0823 과제(계산기2) 교수님 힌트
s = "3+4+5*6+7" # "34+56*+7+"

res = [] # 후위표기법으로 표현된것을 저장
stack = []
i = 0
n = len(s)
while i < n:
    if ord('0') <= ord(s[i]) <= ord('9') :
        res.append(s[i])
    else :
        if s[i] == '+':
            while stack :
                res.append(stack.pop())
            stack.append(s[i])
        if s[i] == '*':
            while stack and stack[-1] == '*' :
                res.append(stack.pop())
            stack.append(s[i])
    i += 1
while stack :
    res.append(stack.pop())

stack = [] # 숫자들을 넣는다

i = 0
while i < n:
    if res[i].isdigit() :
        stack.append(int(res[i]))
    else :
        if res[i] == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        if res[i] == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
    i += 1

print(stack[-1])