def tail(file_name, n=2):
    file = open(file_name)
    text = file.readlines()
    file.close()

    return text[-n:]


result = tail("files/text.txt", 1)
print(result)

result = tail("files/text.txt", 3)
print(result)

result = tail("files/text.txt", 10)
print(result)
