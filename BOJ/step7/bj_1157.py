chars = input()
chars = chars.upper()

result = dict()

for char in chars:
    if char in result.keys():
        result[char] += 1
    else:
        result[char] = 1

