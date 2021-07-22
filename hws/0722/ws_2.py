def get_secret_number(words):
    result = 0
    for word in words:
        result += ord(word)
    return result

num = get_secret_number('tom')
print(num)
