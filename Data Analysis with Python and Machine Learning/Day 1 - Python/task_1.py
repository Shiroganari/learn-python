def head(file_name, n=5):
    file = open(file_name)
    text = file.readlines()
    file.close()

    return text[:n]


result = head("files/text.txt", 2)
print(result)

result = head("files/text.txt", 20)
print(result)
