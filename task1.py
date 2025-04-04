# Программа для считывания данных из файла и вывода их на экран
with open('input.txt', 'r') as file:
    content = file.read()
    print(content)