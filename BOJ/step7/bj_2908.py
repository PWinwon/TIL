number_a, number_b = input().split()

num_a = ''
num_b = ''

for a in range(2,-1,-1):
    num_a += number_a[a]
    num_b += number_b[a]


num_a = int(num_a)
num_b = int(num_b)

if num_a > num_b:
    print(num_a)
else :
    print(num_b)