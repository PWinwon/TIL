alpha_list = [-1] * 26

chars = input()

for c in chars:
    if alpha_list[ord(c)-97] == -1:
        alpha_list[ord(c)-97] = chars.index(c)

for alpha in alpha_list:
    print(alpha, end = ' ')


