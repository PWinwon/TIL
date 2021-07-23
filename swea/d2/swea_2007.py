def find_pattern(chars):
    result_str = ''
    str_len = 0
    for char in chars:
        result_str += char
        str_len = len(chars) // len(result_str)
        if result_str * str_len == chars[0:len(result_str)*str_len]:
            return len(result_str)





T = int(input())
for i in range(T):
    string = input()
    print(f'#{i+1} {find_pattern(string)}')
