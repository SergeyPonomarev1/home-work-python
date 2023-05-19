# Задание 1

from abc import ABC, abstractmethod

# Абстрактный класс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретная команда
class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action()

# Получатель команды
class Receiver:
    def action(self):
        print("Receiver: выполнение действия")

# Инициатор команды
class Invoker:
    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()

# Создаем объекты
receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker()

# Устанавливаем команду для инициатора
invoker.set_command(command)

# Инициатор выполняет команду
invoker.execute_command()

# Задание 2

from abc import ABC, abstractmethod
import time


class NumberSet(ABC):
    @abstractmethod
    def get_numbers(self):
        pass


class FileNumberSet(NumberSet):
    def __init__(self, file_name):
        self.file_name = file_name
        self.numbers = []

    def get_numbers(self):
        with open(self.file_name) as f:
            self.numbers = [int(line.strip()) for line in f.readlines()]
        return self.numbers

    def update(self):
        # implementation of updating mechanism
        print("Updating numbers...")
        time.sleep(5)
        self.get_numbers()


class NumberSetProxy(NumberSet):
    def __init__(self, number_set):
        self.number_set = number_set

    def get_numbers(self):
        numbers = self.number_set.get_numbers()
        self.log_access()
        return numbers

    def log_access(self):
        with open("access.log", "a") as f:
            f.write(f"Accessed at {time.time()}\n")


class NumberSetIterator:
    def __init__(self, number_set):
        self.number_set = number_set
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.number_set.get_numbers()):
            raise StopIteration
        number = self.number_set.get_numbers()[self.index]
        self.index += 1
        return number


if __name__ == "__main__":
    file_number_set = FileNumberSet("numbers.txt")
    number_set_proxy = NumberSetProxy(file_number_set)
    iterator = NumberSetIterator(number_set_proxy)

    # example usage
    print(sum(iterator))
    print(max(iterator))
    print(min(iterator))

    # updating mechanism
    file_number_set.update()


# Задание 3
class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def save_data(self, data):
        # сохранение данных в файл
        pass

    def load_data(self):
        # загрузка данных из файла
        pass

# Реализация паттерна Factory Method для создания объектов книг, библиотекарей и читателей
class EntityFactory:
    def create_book(self, title, author, year):
        return Book(title, author, year)

    def create_librarian(self, name, surname):
        return Librarian(name, surname)

    def create_reader(self, name, surname):
        return Reader(name, surname)

# Реализация паттерна Observer для логгирования действий пользователя
class Logger:
    def log_action(self, action):
        # запись действия в лог-файл
        pass

    def notify(self):
        # уведомление об изменении данных
        pass

# Реализация паттерна Strategy для выбора алгоритма поиска информации о сущностях
class SearchStrategy:
    def search(self, query):
        # поиск информации по запросу
        pass

class BookSearchStrategy(SearchStrategy):
    def search(self, query):
        # поиск книг по запросу
        pass

class LibrarianSearchStrategy(SearchStrategy):
    def search(self, query):
        # поиск библиотекарей по запросу
        pass

class ReaderSearchStrategy(SearchStrategy):
    def search(self, query):
        # поиск читателей по запросу
        pass

# Пример использования паттернов в приложении
class Library:
    def __init__(self):
        self.file_manager = FileManager()
        self.entity_factory = EntityFactory()
        self.logger = Logger()
        self.search_strategy = BookSearchStrategy()

        self.books = []
        self.librarians = []
        self.readers = []

    def add_book(self, title, author, year):
        book = self.entity_factory.create_book(title, author, year)
        self.books.append(book)
        self.logger.log_action(f"Book {title} added")
        self.logger.notify()

    def remove_book(self, book):
        self.books.remove(book)
        self.logger.log_action(f"Book {book.title} removed")
        self.logger.notify()

    def search_books(self, query):
        result = self.search_strategy.search(query)
        return result

    # остальные методы для работы с библиотекарями и читателями

# Пример использования приложения
library = Library()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
library.add_book("1984", "George Orwell", 1949)

result = library.search_books("Orwell")
print(result) # вывод найденных книг на экран или в файл

# сохранение данных в файл
data = {
    "books": library.books,
    "librarians": library.librarians,
    "readers": library.readers
}
file_manager = FileManager()
file_manager.save_data(data)

# загрузка данных из файла
data = file_manager.load_data()
library.books = data["books"]
library.librarians = data["librarians"]
library.readers = data["readers"]