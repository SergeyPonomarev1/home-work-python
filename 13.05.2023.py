# Задание 1
class Student:
    def __init__(self, name="", age=0, gender="", major=""):
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major

    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}, {self.major}"

class StudentBuilder:
    def __init__(self):
        self.student = Student()

    def set_name(self, name):
        self.student.name = name
        return self

    def set_age(self, age):
        self.student.age = age
        return self

    def set_gender(self, gender):
        self.student.gender = gender
        return self

    def set_major(self, major):
        self.student.major = major
        return self

    def build(self):
        return self.student

# Пример использования билдера:

student = (
    StudentBuilder()
    .set_name("Иван")
    .set_age(23)
    .set_gender("мужской")
    .set_major("Математика")
    .build()
)

print(student)

# Задание 2

from abc import ABC, abstractmethod

# Абстрактный класс для макарон
class Pasta(ABC):
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def sauce(self):
        pass

    @abstractmethod
    def filling(self):
        pass

    @abstractmethod
    def toppings(self):
        pass

# Класс для спагетти
class Spaghetti(Pasta):
    def type(self):
        return "Spaghetti"

    def sauce(self):
        return "Tomato sauce"

    def filling(self):
        return "Meatballs"

    def toppings(self):
        return "Parmesan cheese"

# Класс для феттучини
class Fettuccine(Pasta):
    def type(self):
        return "Fettuccine"

    def sauce(self):
        return "Alfredo sauce"

    def filling(self):
        return "Chicken"

    def toppings(self):
        return "Mushrooms"

# Класс для макарони
class Macaroni(Pasta):
    def type(self):
        return "Macaroni"

    def sauce(self):
        return "Cheese sauce"

    def filling(self):
        return "Bacon"

    def toppings(self):
        return "Green onions"

# Фабрика для создания макарон
class PastaFactory:
    def create_pasta(self, pasta_type):
        if pasta_type == "Spaghetti":
            return Spaghetti()
        elif pasta_type == "Fettuccine":
            return Fettuccine()
        elif pasta_type == "Macaroni":
            return Macaroni()
        else:
            return None

# Пример использования
factory = PastaFactory()
spaghetti = factory.create_pasta("Spaghetti")
print(spaghetti.type())       # Spaghetti
print(spaghetti.sauce())      # Tomato sauce
print(spaghetti.filling())    # Meatballs
print(spaghetti.toppings())   # Parmesan cheese

fettuccine = factory.create_pasta("Fettuccine")
print(fettuccine.type())      # Fettuccine
print(fettuccine.sauce())     # Alfredo sauce
print(fettuccine.filling())   # Chicken
print(fettuccine.toppings())  # Mushrooms

macaroni = factory.create_pasta("Macaroni")
print(macaroni.type())        # Macaroni
print(macaroni.sauce())       # Cheese sauce
print(macaroni.filling())     # Bacon
print(macaroni.toppings())    # Green onions

# Задание 3

import copy

# Абстрактный класс для прототипа
class Prototype:
    def clone(self):
        pass

# Класс для конкретного прототипа
class ConcretePrototype(Prototype):
    def __init__(self, value):
        self._value = value

    def clone(self):
        return copy.deepcopy(self)

    def get_value(self):
        return self._value

# Пример использования
prototype = ConcretePrototype(10)
print(prototype.get_value())   # 10

prototype_copy = prototype.clone()
print(prototype_copy.get_value())  # 10

# Изменяем значение копии
prototype_copy._value = 20
print(prototype_copy.get_value())  # 20

# Значение оригинала не изменилось
print(prototype.get_value())   # 10