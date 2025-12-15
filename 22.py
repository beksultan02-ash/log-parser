import os

if os.path.exists('logs.txt'):
    print("Файл существует!")
    file_size = os.path.getsize('logs.txt')
    
    print(f"Размер файла: {file_size} байт")
    
    if file_size > 0:
        with open('logs.txt', 'r') as file:
            content = file.read()
        print("Содержимое файла:")
        print(content)
    else:
        print("Файл существует, но он ПУСТОЙ!")
else:
    print("Файл 'logs.txt' НЕ НАЙДЕН в текущей директории!")