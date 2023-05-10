# Задание 1
# Создание пустого списка
#numbers = []
#
## Основной код программы
#while True:
#    # Показываем меню
#    print("Меню:")
#    print("1. Добавить новое число в список")
#    print("2. Удалить все вхождения числа из списка")
#    print("3. Показать содержимое списка")
#    print("4. Проверить есть ли значение в списке")
#    print("5. Заменить значение в списке")
#    print("6. Выход")
#
#    choice = int(input("Введите номер выбранного пункта меню: "))
#
#    # Используем ветвление if-elif-else для выполнения действий в зависимости от выбора пользователя
#    if choice == 1:
#        num = int(input("Введите число: "))
#        if num in numbers:
#            print("Такое число уже есть в списке")
#        else:
#            numbers.append(num)
#            print("Число успешно добавлено в список")
#    elif choice == 2:
#        num = int(input("Введите число, которое нужно удалить из списка: "))
#        count = numbers.count(num)
#        if count > 0:
#            numbers = [x for x in numbers if x != num]
#            print("Все вхождения числа", num, "успешно удалены из списка")
#        else:
#            print("Числа", num, "нет в списке")
#    elif choice == 3:
#        rev = input("Показать список с начала или с конца? (Введите 'начало' или 'конец'): ")
#        if rev.lower() == 'конец':
#            numbers.reverse()
#        print("Список чисел:", numbers)
#        numbers.reverse()  # Возвращаем список в исходный порядок
#    elif choice == 4:
#        num = int(input("Введите число, которое нужно проверить: "))
#        if num in numbers:
#            print("Число", num, "есть в списке")
#        else:
#            print("Числа", num, "нет в списке")
#    elif choice == 5:
#        num = int(input("Введите число, которое нужно заменить: "))
#        if num not in numbers:
#            print("Числа", num, "нет в списке")
#        else:
#            new_num = int(input("Введите новое число: "))
#            replace_all = input("Заменить все вхождения числа? (Введите 'да' или 'нет'): ")
#            if replace_all.lower() == 'да':
#                numbers = [new_num if x == num else x for x in numbers]
#            else:
#                index = numbers.index(num)
#                numbers[index] = new_num
#            print("Число", num, "успешно заменено на", new_num)
#    elif choice == 6:
#        print("Выход из программы")
#        break
#    else:
#        print("Некорректный выбор")

# Задание 2
#class Stack:
#    def __init__(self, size):
#        self.stack = []
#        self.size = size
#
#    def push(self, string):
#        if len(self.stack) < self.size:
#            self.stack.append(string)
#            print(f"Строка '{string}' успешно добавлена в стек")
#        else:
#            print("Стек полный, строка не добавлена.")
#
#    def pop(self):
#        if len(self.stack) > 0:
#            string = self.stack.pop()
#            print(f"Строка '{string}' удалена из стека")
#        else:
#            print("Стек пуст, удаление невозможно.")
#
#    def count(self):
#        print(f"В стеке {len(self.stack)} строк")
#
#    def is_empty(self):
#        if len(self.stack) == 0:
#            print("Стек пуст")
#        else:
#            print("Стек не пуст")
#
#    def is_full(self):
#        if len(self.stack) == self.size:
#            print("Стек полный")
#        else:
#            print("Стек не полный")
#
#    def clear(self):
#        self.stack.clear()
#        print("Стек очищен")
#
#    def peek(self):
#        if len(self.stack) > 0:
#            string = self.stack[-1]
#            print(f"Последняя добавленная строка в стеке: '{string}'")
#        else:
#            print("Стек пуст")
#
#    def menu(self):
#        while True:
#            print("Меню:")
#            print("1. Добавить строку в стек")
#            print("2. Вытолкнуть строку из стека")
#            print("3. Подсчитать количество строк в стеке")
#            print("4. Проверить, пустой ли стек")
#            print("5. Проверить, полный ли стек")
#            print("6. Очистить стек")
#            print("7. Получить значение без выталкивания верхней строки")
#            print("8. Выход")
#            choice = int(input("Введите номер выбранного пункта меню: "))
#            if choice == 1:
#                string = input("Введите строку для добавления в стек: ")
#                self.push(string)
#            elif choice == 2:
#                self.pop()
#            elif choice == 3:
#                self.count()
#            elif choice == 4:
#                self.is_empty()
#            elif choice == 5:
#                self.is_full()
#            elif choice == 6:
#                self.clear()
#            elif choice == 7:
#                self.peek()
#            elif choice == 8:
#                print("Выход из программы")
#                break
#            else:
#                print("Некорректный выбор")
#
#stack = Stack(3)
#stack.menu()

# Задание 3
#class Stack:
#    def __init__(self):
#        self.stack = []
#
#    def push(self, string):
#        self.stack.append(string)
#        print(f"Строка '{string}' успешно добавлена в стек")
#
#    def pop(self):
#        if len(self.stack) > 0:
#            string = self.stack.pop()
#            print(f"Строка '{string}' удалена из стека")
#        else:
#            print("Стек пуст, удаление невозможно.")
#
#    def count(self):
#        print(f"В стеке {len(self.stack)} строк")
#
#    def is_empty(self):
#        if len(self.stack) == 0:
#            print("Стек пуст")
#        else:
#            print("Стек не пуст")
#
#    def clear(self):
#        self.stack.clear()
#        print("Стек очищен")
#
#    def peek(self):
#        if len(self.stack) > 0:
#            string = self.stack[-1]
#            print(f"Последняя добавленная строка в стеке: '{string}'")
#        else:
#            print("Стек пуст")
#
#    def menu(self):
#        while True:
#            print("Меню:")
#            print("1. Добавить строку в стек")
#            print("2. Вытолкнуть строку из стека")
#            print("3. Подсчитать количество строк в стеке")
#            print("4. Проверить, пустой ли стек")
#            print("5. Очистить стек")
#            print("6. Получить значение без выталкивания верхней строки")
#            print("7. Выход")
#            choice = int(input("Введите номер выбранного пункта меню: "))
#            if choice == 1:
#                string = input("Введите строку для добавления в стек: ")
#                self.push(string)
#            elif choice == 2:
#                self.pop()
#            elif choice == 3:
#                self.count()
#            elif choice == 4:
#                self.is_empty()
#            elif choice == 5:
#                self.clear()
#            elif choice == 6:
#                self.peek()
#            elif choice == 7:
#                print("Выход из программы")
#                break
#            else:
#                print("Некорректный выбор")
#
#
#stack = Stack()
#stack.menu()