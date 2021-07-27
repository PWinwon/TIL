def duplicated_letters(letters):
    result = []
    for letter in letters:
        if letters.count(letter) > 1 and letter not in result:
            result.append(letter)
    return result
a = duplicated_letters('apple')
b = duplicated_letters('banana')
print(a)
print(b)