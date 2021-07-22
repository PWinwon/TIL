def get_secret_word(words):
    result_list = ''
    for word in words:
        result_list += chr(word)
    return result_list

result = get_secret_word([83, 115, 65, 102, 89])

print(result)