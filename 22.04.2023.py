# Задание 1
#class Circle:
#    def __init__(self, radius):
#        self.radius = radius
#
#    def __eq__(self, other):
#        return self.radius == other.radius
#
#    def __lt__(self, other):
#        return 2 * self.radius < 2 * other.radius
#
#    def __le__(self, other):
#        return 2 * self.radius <= 2 * other.radius
#
#    def __gt__(self, other):
#        return 2 * self.radius > 2 * other.radius
#
#    def __ge__(self, other):
#        return 2 * self.radius >= 2 * other.radius
#
#    def __add__(self, other):
#        return Circle(self.radius + other)
#
#    def __radd__(self, other):
#        return Circle(self.radius + other)
#
#    def __iadd__(self, other):
#        self.radius += other
#        return self
#
#    def __sub__(self, other):
#        return Circle(self.radius - other)
#
#    def __rsub__(self, other):
#        return Circle(other - self.radius)
#
#    def __isub__(self, other):
#        self.radius -= other
#        return self
#
#    def __repr__(self):
#        return f"Circle({self.radius})"
#
#    def __str__(self):
#        return f"Circle with radius {self.radius}"

# Задание 2
#class Complex:
#    def __init__(self, real, imag):
#        self.real = real
#        self.imag = imag
#
#    def __add__(self, other):
#        return Complex(self.real + other.real, self.imag + other.imag)
#
#    def __sub__(self, other):
#        return Complex(self.real - other.real, self.imag - other.imag)
#
#    def __mul__(self, other):
#        return Complex(self.real * other.real - self.imag * other.imag,
#                       self.real * other.imag + self.imag * other.real)
#
#    def __truediv__(self, other):
#        denominator = float(other.real ** 2 + other.imag ** 2)
#        return Complex((self.real * other.real + self.imag * other.imag) / denominator,
#                       (self.imag * other.real - self.real * other.imag) / denominator)
#
#    def __repr__(self):
#        return f"Complex({self.real}, {self.imag})"
#
#    def __str__(self):
#        sign = "+" if self.imag >= 0 else "-"
#        return f"{self.real} {sign} {abs(self.imag)}i"


# Задание 3
#class Airplane:
#    def __init__(self, model, max_passengers, num_passengers=0):
#        self.model = model
#        self.max_passengers = max_passengers
#        self.num_passengers = num_passengers
#
#    def __eq__(self, other):
#        return self.model == other.model
#
#    def __add__(self, other):
#        new_num_passengers = self.num_passengers + other
#        if new_num_passengers <= self.max_passengers:
#            self.num_passengers = new_num_passengers
#        else:
#            raise ValueError("Too many passengers")
#        return self
#
#    def __radd__(self, other):
#        return self + other
#
#    def __iadd__(self, other):
#        return self + other
#
#    def __sub__(self, other):
#        new_num_passengers = self.num_passengers - other
#        if new_num_passengers >= 0:
#            self.num_passengers = new_num_passengers
#        else:
#            raise ValueError("Too few passengers")
#        return self
#
#    def __rsub__(self, other):
#        raise NotImplementedError("Cannot subtract airplane from number")
#
#    def __isub__(self, other):
#        return self - other
#
#    def __lt__(self, other):
#        return self.max_passengers < other.max_passengers
#
#    def __le__(self, other):
#        return self.max_passengers <= other.max_passengers
#
#    def __gt__(self, other):
#        return self.max_passengers > other.max_passengers
#
#    def __ge__(self, other):
#        return self.max_passengers >= other.max_passengers
#
#    def __repr__(self):
#        return f"Airplane({self.model}, {self.max_passengers}, {self.num_passengers})"
#
#    def __str__(self):
#        return f"{self.model} airplane with {self.num_passengers} passengers"

# Задание 4
#class Flat:
#    def __init__(self, area, price):
#        self.area = area
#        self.price = price
#
#    def __eq__(self, other):
#        return self.area == other.area
#
#    def __ne__(self, other):
#        return not self == other
#
#    def __lt__(self, other):
#        return self.price < other.price
#
#    def __le__(self, other):
#        return self.price <= other.price
#
#    def __gt__(self, other):
#        return self.price > other.price
#
#    def __ge__(self, other):
#        return self.price >= other.price
#
#    def __repr__(self):
#        return f"Flat({self.area}, {self.price})"
#
#    def __str__(self):
#        return f"Flat with area {self.area} and price {self.price}"