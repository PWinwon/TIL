def reversed_str(chars):
    if len(chars) < 2:
        return 1
    if chars[-1] == chars[0]:
        return reversed_str(chars[1:-1])
    else:
        return 0

T = int(input())

for i in range(T):
    string = input()
    result = reversed_str(string)
    print(f'#{i+1} {result}')