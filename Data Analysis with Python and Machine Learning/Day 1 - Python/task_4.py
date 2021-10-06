def cleanup(text, bad_chars):
    for bad_char in bad_chars:
        text = text.replace(bad_char, '')
    return text


result = cleanup('hello,\tworld!\n', '\n \t ')
print(result)

result = cleanup('dict([(1, "one"), (2, "two")])', '(", ")')
print(result)
