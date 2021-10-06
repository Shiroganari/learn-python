def wc2(file_name):
    file = open(file_name)
    text = file.read()
    file.close()

    lines_count = len(text.split("\n"))
    words_count = len(text.split())
    chars_count = 0

    for char in text:
        if char != "\n" and char != "\t" and char != " ":
            chars_count += 1

    return lines_count, words_count, chars_count


result = wc2("files/text.txt")
print(result)
