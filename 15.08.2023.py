#Задание 1
#class Car:
#    def __init__(self, model, year, manufacturer, engine_volume, color, price):
#        self.model = model
#        self.year = year
#        self.manufacturer = manufacturer
#        self.engine_volume = engine_volume
#        self.color = color
#        self.price = price
#
#    def set_model(self, model):
#        self.model = model
#
#    def set_year(self, year):
#        self.year = year
#
#    def set_manufacturer(self, manufacturer):
#        self.manufacturer = manufacturer
#
#    def set_engine_volume(self, engine_volume):
#        self.engine_volume = engine_volume
#
#    def set_color(self, color):
#        self.color = color
#
#    def set_price(self, price):
#        self.price = price
#
#    def get_model(self):
#        return self.model
#
#    def get_year(self):
#        return self.year
#
#    def get_manufacturer(self):
#        return self.manufacturer
#
#    def get_engine_volume(self):
#        return self.engine_volume
#
#    def get_color(self):
#        return self.color
#
#    def get_price(self):
#        return self.price
#
#    def display_car_info(self):
#        print(f"Модель: {self.model}")
#        print(f"Год выпуска: {self.year}")
#        print(f"Производитель: {self.manufacturer}")
#        print(f"Объем двигателя: {self.engine_volume}")
#        print(f"Цвет: {self.color}")
#        print(f"Цена: {self.price}")
#
#    def enter_car_info(self):
#        model = input("Введите модель автомобиля: ")
#        year = int(input("Введите год выпуска: "))
#        manufacturer = input("Введите производителя: ")
#        engine_volume = float(input("Введите объем двигателя: "))
#        color = input("Введите цвет: ")
#        price = float(input("Введите цену: "))
#        self.set_model(model)
#        self.set_year(year)
#        self.set_manufacturer(manufacturer)
#        self.set_engine_volume(engine_volume)
#        self.set_color(color)
#        self.set_price(price)
#
#car = Car('Mercedes', 2022, 'Mercedes-Benz', 3.5, 'черный', 1000000)
#car.display_car_info()
#car.set_price(1200000)
#print(f"Новая цена: {car.get_price()}")
#car.enter_car_info()
#car.display_car_info()

#Задание 2
#class Book:
#    def __init__(self, title, year, publisher, genre, author, price):
#        self.title = title
#        self.year = year
#        self.publisher = publisher
#        self.genre = genre
#        self.author = author
#        self.price = price
#
#    def set_title(self, title):
#        self.title = title
#
#    def set_year(self, year):
#        self.year = year
#
#    def set_publisher(self, publisher):
#        self.publisher = publisher
#
#    def set_genre(self, genre):
#        self.genre = genre
#
#    def set_author(self, author):
#        self.author = author
#
#    def set_price(self, price):
#        self.price = price
#
#    def get_title(self):
#        return self.title
#
#    def get_year(self):
#        return self.year
#
#    def get_publisher(self):
#        return self.publisher
#
#    def get_genre(self):
#        return self.genre
#
#    def get_author(self):
#        return self.author
#
#    def get_price(self):
#        return self.price
#
#    def display_book_info(self):
#        print(f"Название: {self.title}")
#        print(f"Год выпуска: {self.year}")
#        print(f"Издатель: {self.publisher}")
#        print(f"Жанр: {self.genre}")
#        print(f"Автор: {self.author}")
#        print(f"Цена: {self.price}")
#
#    def enter_book_info(self):
#        title = input("Введите название книги: ")
#        year = int(input("Введите год выпуска: "))
#        publisher = input("Введите издателя: ")
#        genre = input("Введите жанр: ")
#        author = input("Введите автора: ")
#        price = float(input("Введите цену: "))
#        self.set_title(title)
#        self.set_year(year)
#        self.set_publisher(publisher)
#        self.set_genre(genre)
#        self.set_author(author)
#        self.set_price(price)
#
#book = Book('Мастер и Маргарита', 1967, 'Москва', 'роман', 'Михаил Булгаков', 500)
#book.display_book_info()
#book.set_price(600)
#print(f"Новая цена: {book.get_price()}")
#book.enter_book_info()
#book.display_book_info()

#Задание 3
#class Stadium:
#    def __init__(self, name, opening_date, country, city, capacity):
#        self.name = name
#        self.opening_date = opening_date
#        self.country = country
#        self.city = city
#        self.capacity = capacity
#
#    def set_name(self, name):
#        self.name = name
#
#    def set_opening_date(self, opening_date):
#        self.opening_date = opening_date
#
#    def set_country(self, country):
#        self.country = country
#
#    def set_city(self, city):
#        self.city = city
#
#    def set_capacity(self, capacity):
#        self.capacity = capacity
#
#    def get_name(self):
#        return self.name
#
#    def get_opening_date(self):
#        return self.opening_date
#
#    def get_country(self):
#        return self.country
#
#    def get_city(self):
#        return self.city
#
#    def get_capacity(self):
#        return self.capacity
#
#    def display_stadium_info(self):
#        print(f"Название: {self.name}")
#        print(f"Дата открытия: {self.opening_date}")
#        print(f"Страна: {self.country}")
#        print(f"Город: {self.city}")
#        print(f"Вместимость: {self.capacity}")
#
#    def enter_stadium_info(self):
#        name = input("Введите название стадиона: ")
#        opening_date = input("Введите дату открытия: ")
#        country = input("Введите страну: ")
#        city = input("Введите город: ")
#        capacity = int(input("Введите вместимость: "))
#        self.set_name(name)
#        self.set_opening_date(opening_date)
#        self.set_country(country)
#        self.set_city(city)
#        self.set_capacity(capacity)
#
#
#name = input("Введите название стадиона: ")
#location = input("Введите дату открытия: ")
#capacity = input("Введите страну в которой находится стадион: ")
#city = input("Введите город в котором находится стадион: ")
#capacity = input("Введите вместимость стадиона: ")
#print("Название стадиона:")
#print("Дата открытия:", name)
#print("Страна:", location)
#print("Город:", city)
#print("Вместимость:", capacity)