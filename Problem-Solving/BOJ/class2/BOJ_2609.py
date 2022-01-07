A, B = map(int, input().split())

if A < B:
    A, B = B, A

gcd = B
lcm = A * B

while True:
    glbg = A % gcd

    if glbg == 0:
        lcm = lcm // gcd
        break
    A = gcd
    gcd = glbg

print(gcd)
print(lcm)