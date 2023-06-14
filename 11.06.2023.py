# Задание 1
#def analysis_and_summarize_file(file_name):
#    # Чтение содержимого файла
#    with open(file_name, 'r') as file:
#        text = file.read()
#
#    # Анализ данных
#    words = text.split()
#    num_lines = text.count('\n')
#    avg_word_length = sum(len(word) for word in words) / len(words)
#    word_freq = {}
#    for word in words:
#        if word in word_freq:
#            word_freq[word] += 1
#        else:
#            word_freq[word] = 1
#
#    # Создание сводного отчета
#    report = f"Number of lines: {num_lines}\n" \
#             f"Average word length: {avg_word_length:.2f}\n" \
#             f"Word frequency:\n"
#    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
#        report += f"{word}: {freq}\n"
#
#    # Запись отчета в новый файл
#    with open("summary.txt", 'w') as file:
#        file.write(report)
#
## Пример использования
#analysis_and_summarize_file("text.txt")

# Задание 2
#import time
#
#def encryption_logging(func):
#    def wrapper(file_name, key):
#        print(f"Encryption/Decryption operation on file {file_name} with key {key} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
#        return func(file_name, key)
#    return wrapper
#
#@encryption_logging
#def encrypt_file(file_name, key):
#    # Чтение содержимого файла
#    with open(file_name, 'r') as file:
#        text = file.read()
#
#    # Шифрование данных
#    encrypted_text = ""
#    for char in text:
#        encrypted_text += chr(ord(char) + key)
#
#    # Запись зашифрованных данных в новый файл
#    with open("encrypted.txt", 'w') as file:
#        file.write(encrypted_text)
#
#@encryption_logging
#def decrypt_file(file_name, key):
#    # Чтение содержимого файла
#    with open(file_name, 'r') as file:
#        encrypted_text = file.read()
#
#    # Расшифровка данных
#    decrypted_text = ""
#    for char in encrypted_text:
#        decrypted_text += chr(ord(char) - key)
#
#    # Запись расшифрованных данных в новый файл
#    with open("decrypted.txt", 'w') as file:
#        file.write(decrypted_text)
#
## Пример использования
#encrypt_file("text.txt", 5)
#decrypt_file("encrypted.txt", 5)

# Задание 3
##print(analysis_file_sizes("/path/to/directory"))