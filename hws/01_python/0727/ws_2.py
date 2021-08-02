def low_and_up(letters):
    result = ''
    for i in range(len(letters)):
        if i % 2 == 1:
            result += letters[i].upper()
        else:
            result += letters[i].lower()
    return result

a = low_and_up('apple')
b = low_and_up('banana')
print(a)
print(b)