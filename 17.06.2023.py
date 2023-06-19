# 1
class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, email, phone):
        customer = Customer(name, email, phone)
        self.customers.append(customer)

    def update_customer(self, name, email, phone):
        for customer in self.customers:
            if customer.name == name:
                customer.email = email
                customer.phone = phone
                break

    def get_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ProductInventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)

    def update_product(self, name, price, quantity):
        for product in self.products:
            if product.name == name:
                product.price = price
                product.quantity = quantity
                break

    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None


# 2
class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

class FictionBook(Book):
    def __init__(self, title, author, publisher, year, genre):
        super().__init__(title, author, publisher, year)
        self.genre = genre

class NonFictionBook(Book):
    def __init__(self, title, author, publisher, year, topic):
        super().__init__(title, author, publisher, year)
        self.topic = topic

class ReferenceBook(Book):
    def __init__(self, title, author, publisher, year, subject):
        super().__init__(title, author, publisher, year)
        self.subject = subject

# Пример использования

fiction_book = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons", 1925, "Jazz Age novel")
non_fiction_book = NonFictionBook("The Selfish Gene", "Richard Dawkins", "Oxford University Press", 1976, "Evolutionary biology")
reference_book = ReferenceBook("The Oxford English Dictionary", "Various", "Oxford University Press", 1884, "English language")

print(fiction_book.title)
print(non_fiction_book.author)
print(reference_book.publisher)

# 3
class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        # Assume triangle is isosceles
        side = ((self.base / 2) ** 2 + self.height ** 2) ** 0.5
        return 2 * side + self.base

# Пример использования

circle = Circle(5)
rectangle = Rectangle(3, 4)
triangle = Triangle(6, 8)

print(circle.calculate_area())
print(rectangle.calculate_perimeter())
print(triangle.calculate_area())

# 4
class TextMessaging:
    def send_text_message(self, message):
        pass

    def receive_text_message(self):
        pass

    def get_message_history(self):
        pass

class MultimediaMessaging:
    def send_multimedia_message(self, message, media_type):
        pass

    def receive_multimedia_message(self):
        pass

    def view_media_gallery(self):
        pass

class TextMessagingService(TextMessaging):
    def send_text_message(self, message):
        # implementation for sending text message
        pass

    def receive_text_message(self):
        # implementation for receiving text message
        pass

    def get_message_history(self):
        # implementation for getting message history
        pass

class MultimediaMessagingService(MultimediaMessaging, TextMessaging):
    def send_multimedia_message(self, message, media_type):
        # implementation for sending multimedia message
        pass

    def receive_multimedia_message(self):
        # implementation for receiving multimedia message
        pass

    def view_media_gallery(self):
        # implementation for viewing media gallery
        pass

    def send_text_message(self, message):
        # implementation for sending text message
        pass

    def receive_text_message(self):
        # implementation for receiving text message
        pass

    def get_message_history(self):
        # implementation for getting message history
        pass

# Пример использования

text_service = TextMessagingService()
multimedia_service = MultimediaMessagingService()

text_service.send_text_message("Hello!")
multimedia_service.send_multimedia_message("Check out this picture!", "image")
multimedia_service.send_text_message("This is a text message.")

# 5
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log_info(self, message):
        pass

    @abstractmethod
    def log_warning(self, message):
        pass

    @abstractmethod
    def log_error(self, message):
        pass

class ConsoleLogger(Logger):
    def log_info(self, message):
        print(f"[INFO] {message}")

    def log_warning(self, message):
        print(f"[WARNING] {message}")

    def log_error(self, message):
        print(f"[ERROR] {message}")

class FileLogger(Logger):
    def __init__(self, file_name):
        self.file_name = file_name

    def log_info(self, message):
        with open(self.file_name, "a") as f:
            f.write(f"[INFO] {message}\n")

    def log_warning(self, message):
        with open(self.file_name, "a") as f:
            f.write(f"[WARNING] {message}\n")

    def log_error(self, message):
        with open(self.file_name, "a") as f:
            f.write(f"[ERROR] {message}\n")

class DatabaseLogger(Logger):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def log_info(self, message):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO logs (level, message) VALUES (?, ?)", ("INFO", message))
        self.db_connection.commit()

    def log_warning(self, message):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO logs (level, message) VALUES (?, ?)", ("WARNING", message))
        self.db_connection.commit()

    def log_error(self, message):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO logs (level, message) VALUES (?, ?)", ("ERROR", message))
        self.db_connection.commit()

# Пример использования

console_logger = ConsoleLogger()
file_logger = FileLogger("log.txt")
database_logger = DatabaseLogger(db_connection)

console_logger.log_info("Informational message")
file_logger.log_warning("Warning message")
database_logger.log_error("Error message")