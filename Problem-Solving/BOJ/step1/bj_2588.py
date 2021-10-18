a = int(input())
b = int(input())
result = a*b

num = [0] * 3

for i in range(0,3):
    num[i] = (b % 10) * a
    b = b // 10
    print(num[i])

print(result)

# 각 자리수 따로 뽑아내는 방법
# n_1 = b % 10
# n_10 = b % 100 - n_1
# n_100 = b - n_1 - n_10