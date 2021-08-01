#좌표 받아서 몇 사분면에 속하는지

x = int(input())
y = int(input())

result = 0

if( x > 0):
    if(y > 0):
        result = 1
    else:
        result = 4
else:
    if(y > 0):
        result = 2
    else:
        result = 3

print(result)
