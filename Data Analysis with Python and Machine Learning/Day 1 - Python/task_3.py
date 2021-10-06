def wc1(file_name):
    file = open(file_name)
    text = file.read()
    file.close()

    lines_count = len(text.split("\n"))
    words_count = len(text.split())
    chars_count = len(text)

    return lines_count, words_count, chars_count


result = wc1("files/text.txt")
print(result)
