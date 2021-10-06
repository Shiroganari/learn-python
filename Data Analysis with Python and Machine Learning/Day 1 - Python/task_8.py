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


def top_words1(file_name, n=5):
    d = wc4(file_name)

    words = [(key, value) for key, value in d.items()]
    words.sort(key=lambda x: x[1], reverse=True)

    return words[:n]


result = top_words1("files/text.txt")
print(result)

result = top_words1("files/text2.txt", 10)
print(result)
