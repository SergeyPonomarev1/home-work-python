# Задание 1
#import json
#import pickle
#
#
#class Car:
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#
#    def drive(self):
#        print(f"{self.make} {self.model} is driving")
#
#    def to_json(self):
#        return json.dumps(self.__dict__)
#
#    def from_json(self, data):
#        self.__dict__ = json.loads(data)
#
#    def to_pickle(self, file_name):
#        with open(file_name, 'wb') as f:
#            pickle.dump(self, f)
#        print(f"Данные сохранены в файл: {file_name}")
#
#    def from_pickle(self, file_name):
#        with open(file_name, 'rb') as f:
#            obj = pickle.load(f)
#        self.__dict__ = obj.__dict__
#        print(f"Данные загружены из файла: {file_name}")
#
#
## Создаем объект класса Car
#car = Car("Toyota", "Corolla", 2021)
#
## Сохраняем данные в формате json
#json_data = car.to_json()
#print(json_data)
#
## Создаем новый объект класса Car и загружаем данные из json-строки
#new_car = Car("", "", "")
#new_car.from_json(json_data)
#new_car.drive()
#
## Сохраняем объект класса Car в файл с помощью pickle
#file_name = "car.pickle"
#car.to_pickle(file_name)
#
## Загружаем данные из файла и создаем новый объект класса Car
#new_car = Car("", "", "")
#new_car.from_pickle(file_name)
#new_car.drive()


# Задание 2
#import json
#import pickle
#
#
#class Book:
#    def __init__(self, title, author, year, pages):
#        self.title = title
#        self.author = author
#        self.year = year
#        self.pages = pages
#
#    def read(self):
#        print(f"Reading {self.title} by {self.author}")
#
#    def to_json(self):
#        return json.dumps(self.__dict__)
#
#    def from_json(self, data):
#        self.__dict__ = json.loads(data)
#
#    def to_pickle(self, file_name):
#        with open(file_name, 'wb') as f:
#            pickle.dump(self, f)
#        print(f"Данные сохранены в файл: {file_name}")
#
#    def from_pickle(self, file_name):
#        with open(file_name, 'rb') as f:
#            obj = pickle.load(f)
#        self.__dict__ = obj.__dict__
#        print(f"Данные загружены из файла: {file_name}")
#
#
#
## Создаем объект класса Book
#book = Book("War and Peace", "Leo Tolstoy", 1869, 1225)
#
## Сохраняем данные в формате json
#json_data = book.to_json()
#print(json_data)
#
## Создаем новый объект класса Book и загружаем данные из json-строки
#new_book = Book("", "", 0, 0)
#new_book.from_json(json_data)
#new_book.read()
#
## Сохраняем объект класса Book в файл с помощью pickle
#file_name = "book.pickle"
#book.to_pickle(file_name)
#
## Загружаем данные из файла и создаем новый объект класса Book
#new_book = Book("", "", 0, 0)
#new_book.from_pickle(file_name)
#new_book.read()

# Задание 3
#import json
#import pickle
#
#class Stadium:
#    def __init__(self, name, location, capacity):
#        self.name = name
#        self.location = location
#        self.capacity = capacity
#
#    def __str__(self):
#        return f"{self.name} ({self.location}) - {self.capacity} seats"
#
#    def pack_json(self):
#        data = {
#            "name": self.name,
#            "location": self.location,
#            "capacity": self.capacity
#        }
#        return json.dumps(data)
#
#    def unpack_json(self, data):
#        data = json.loads(data)
#        self.name = data.get("name", "")
#        self.location = data.get("location", "")
#        self.capacity = data.get("capacity", 0)
#
#    def pack_pickle(self):
#        return pickle.dumps(self)
#
#    @classmethod
#    def unpack_pickle(cls, data):
#        obj = pickle.loads(data)
#        return cls(obj.name, obj.location, obj.capacity)
#
#stadium = Stadium("Soccer City", "Johannesburg", 94736)
#
## Pack to JSON
#json_data = stadium.pack_json()
#print(json_data)
#
## Unpack from JSON
#stadium_from_json = Stadium("", "", 0)
#stadium_from_json.unpack_json(json_data)
#print(stadium_from_json)
#
## Pack to Pickle
#pickle_data = stadium.pack_pickle()
#print(pickle_data)
#
## Unpack from Pickle
#stadium_from_pickle = Stadium.unpack_pickle(pickle_data)
#print(stadium_from_pickle)