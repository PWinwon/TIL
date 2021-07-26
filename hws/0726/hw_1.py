def count_vowels(strings):
    cnt = 0
    moum = ['a', 'e', 'i', 'o', 'u', 'w', 'y']
    for m in moum:
        cnt += strings.count(m)
    return cnt


p1 = count_vowels('apple')
p2 = count_vowels('banana')

print(p1)
print(p2)
