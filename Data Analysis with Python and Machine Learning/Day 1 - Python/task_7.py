def cleanup(text, bad_chars):
    for bad_char in bad_chars:
        text = text.replace(bad_char, '')
    return text


def wc4(file_name):
    file = open(file_name)
    text = file.read()
    file.close()

    file = open('files/stopwords.txt')
    stopwords = file.read().split()
    file.close()

    text = text.lower()
    text = cleanup(text, ['can\'t', 'ain\'t', '\'m', '\'ve', '\'ll', '\'d', '\'re', '\'ve', '\'s', 'n\'t'])
    text = cleanup(text, '~`!@#$%^&*()[]{}_-+=;:\'"\\|,<.>/?')

    words = text.split()
    words = [value for value in words if value not in stopwords]

    d = dict().fromkeys(words, 0)
    for word in words:
        d[word] += 1

    return d


result = wc4("files/text.txt")
print(result)

result = wc4("files/text2.txt")
print(result)
