fibo_lst = [0, 1]
while fibo_lst[-1] < 100000:
    fibo_lst.append(fibo_lst[-1] + fibo_lst[-2])

D, K = map(int, input().split())
# D 에 대해 K = fibo_lst[D-2] * A + fibo_lst[D-1] * B
A = 1
B = 1
a = fibo_lst[D-2]
b = fibo_lst[D-1]
while True:
    if A*a + B*b == K:
        break
    if A*a + B*b > K:
        A += 1
        B = A
        continue
    B += 1
print(A)
print(B)