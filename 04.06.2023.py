# Задание 1
#def analysis_and_summarize_file(file_name):
#    # Открыть файл и прочитать содержимое
#    with open(file_name, 'r') as f:
#        content = f.read()
#
#    # Создать счетчик слов
#    word_count = {}
#    words = content.split()
#    for word in words:
#        if word in word_count:
#            word_count[word] += 1
#        else:
#            word_count[word] = 1
#
#    # Посчитать общее количество слов
#    total_words = sum(word_count.values())
#
#    # Посчитать количество строк
#    lines = content.split('\n')
#    line_count = len(lines)
#
#    # Посчитать среднюю длину слова
#    total_length = sum(len(word) for word in words)
#    average_length = total_length / total_words
#
#    # Создать сводный отчет
#    report = f'Содержимое файла {file_name}:\n\n'
#    report += f'Количество строк: {line_count}\n'
#    report += f'Общее количество слов: {total_words}\n'
#    report += f'Средняя длина слова: {average_length:.2f}\n'
#    report += '\nЧастота слов:\n'
#    for word, count in word_count.items():
#        report += f'{word}: {count}\n'
#
#    # Создать новый файл и записать сводный отчет
#    report_file_name = file_name + '_report.txt'
#    with open(report_file_name, 'w') as f:
#        f.write(report)
#
#    print(f'Сводный отчет сохранен в файле {report_file_name}')

# Задание 2
#import datetime
#
#def encrypt_file(file_name, key):
#    # Открыть файл и прочитать содержимое
#    with open(file_name, 'r') as f:
#        content = f.read()
#
#    # Шифровать содержимое
#    encrypted_content = content + key
#
#    # Создать новый файл и записать зашифрованные данные
#    encrypted_file_name = file_name + '_encrypted.txt'
#    with open(encrypted_file_name, 'w') as f:
#        f.write(encrypted_content)
#
#    print(f'Файл {file_name} был зашифрован и записан в файл {encrypted_file_name}')
#
#def decrypt_file(file_name, key):
#    # Открыть файл и прочитать содержимое
#    with open(file_name, 'r') as f:
#        content = f.read()
#
#    # Расшифровать содержимое
#    decrypted_content = content[:-len(key)]
#
#    # Создать новый файл и записать расшифрованные данные
#    decrypted_file_name = file_name + '_decrypted.txt'
#    with open(decrypted_file_name, 'w') as f:
#        f.write(decrypted_content)
#
#    print(f'Файл {file_name} был расшифрован и записан в файл {decrypted_file_name}')
#
#
# А вот декоратор encryption_logging:
#
#
#def encryption_logging(func):
#    def wrapper(file_name, key):
#        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#        print(f'[{now}] Начало операции {func.__name__} для файла {file_name} с ключом {key}')
#        func(file_name, key)
#        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#        print(f'[{now}] Окончание операции {func.__name__} для файла {file_name} с ключом {key}')
#
#    return wrapper

# Задание 3
#import os
#
#def analysis_file_sizes(path):
#    total_size = 0
#    for root, dirs, files in os.walk(path):
#        for file in files:
#            file_path = os.path.join(root, file)
#            total_size += os.path.getsize(file_path)
#
#    # Вычислить единицы измерения
#    units = ['Б', 'КБ', 'МБ', 'ГБ']
#    index = 0
#    while total_size >= 1024 and index < len(units) - 1:
#        total_size /= 1024
#        index += 1
#
#    # Форматировать результат и вернуть
#    return f'Размер файлов в каталоге {path}: {total_size:.2f} {units[index]}'
#

#Эта функция использует модуль os для обхода каталога и его подкаталогов, нахождения всех файлов и вычисления их общего размера. Затем она вычисляет соответствуюущие единицы измерения и форматирует результат.
#
#Теперь можно вызвать функцию analysis_file_sizes со следующим кодом:

#print(analysis_file_sizes('path/to/directory'))