a= int(input())
b= int(input())
c= int(input())

abc = a * b * c
result = [0] * 10

for i in str(abc):
    j = int(i)
    result[j] += 1

for k in range(0,10):
    print(result[k])