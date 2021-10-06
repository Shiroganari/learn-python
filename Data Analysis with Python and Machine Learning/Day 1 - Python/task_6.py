def cleanup(text, bad_chars):
    for bad_char in bad_chars:
        text = text.replace(bad_char, '')
    return text


def wc3(file_name):
    file = open(file_name)
    text = file.read()
    file.close()

    text = text.lower()
    text = cleanup(text, ['can\'t', 'ain\'t', '\'m', '\'ve', '\'ll', '\'d', '\'re', '\'ve', '\'s', 'n\'t'])
    text = cleanup(text, '~`!@#$%^&*()[]{}_-+=;:\'"\\|,<.>/?')

    words = text.split()

    d = dict().fromkeys(words, 0)
    for word in words:
        d[word] += 1

    return d


result = wc3("files/text.txt")
print(result)

result = wc3("files/text2.txt")
print(result)
