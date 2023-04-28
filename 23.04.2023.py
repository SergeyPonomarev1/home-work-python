# Задание 1
#import math
#
#class Figure:
#    def area(self):
#        pass
#
#class Rectangle(Figure):
#    def __init__(self, width, height):
#        self.width = width
#        self.height = height
#
#    def area(self):
#        return self.width * self.height
#
#class Circle(Figure):
#    def __init__(self, radius):
#        self.radius = radius
#
#    def area(self):
#        return math.pi * self.radius ** 2
#
#class RightTriangle(Figure):
#    def __init__(self, base, height):
#        self.base = base
#        self.height = height
#
#    def area(self):
#        return 0.5 * self.base * self.height
#
#class Trapezoid(Figure):
#    def __init__(self, base1, base2, height):
#        self.base1 = base1
#        self.base2 = base2
#        self.height = height
#
#    def area(self):
#        return 0.5 * (self.base1 + self.base2) * self.height

# Задание 2
#import math
#
#class Figure:
#    def area(self):
#        pass
#
#    def __int__(self):
#        return self.area()
#
#    def __str__(self):
#        return f"{self.__class__.__name__}"
#
#class Rectangle(Figure):
#    def __init__(self, width, height):
#        self.width = width
#        self.height = height
#
#    def area(self):
#        return self.width * self.height
#
#    def __str__(self):
#        return f"{super().__str__()} with width {self.width} and height {self.height}"
#
#class Circle(Figure):
#    def __init__(self, radius):
#        self.radius = radius
#
#    def area(self):
#        return math.pi * self.radius ** 2
#
#    def __str__(self):
#        return f"{super().__str__()} with radius {self.radius}"
#
#class RightTriangle(Figure):
#    def __init__(self, base, height):
#        self.base = base
#        self.height = height
#
#    def area(self):
#        return 0.5 * self.base * self.height
#
#    def __str__(self):
#        return f"{super().__str__()} with base {self.base} and height {self.height}"
#
#class Trapezoid(Figure):
#    def __init__(self, base1, base2, height):
#        self.base1 = base1
#        self.base2 = base2
#        self.height = height
#
#    def area(self):
#        return 0.5 * (self.base1 + self.base2) * self.height
#
#    def __str__(self):
#        return f"{super().__str__()} with bases {self.base1} and {self.base2} and height {self.height}"


# Задание 3
#class Shape:
#    def show(self):
#        pass
#
#    def save(self, filename):
#        pass
#
#    @classmethod
#    def load(cls, filename):
#        pass
#
#class Square(Shape):
#    def __init__(self, x, y, size):
#        self.x = x
#        self.y = y
#        self.size = size
#
#    def show(self):
#        print(f"Square with upper left corner at ({self.x}, {self.y}) and size {self.size}")
#
#    def save(self, filename):
#        with open(filename, "a") as f:
#            f.write(f"Square {self.x} {self.y} {self.size}\n")
#
#    @classmethod
#    def load(cls, filename):
#        squares = []
#        with open(filename, "r") as f:
#            lines = f.readlines()
#            for line in lines:
#                data = line.strip().split()
#                if data[0] == "Square":
#                    x = int(data[1])
#                    y = int(data[2])
#                    size = int(data[3])
#                    square = Square(x, y, size)
#                    squares.append(square)
#        return squares
#
#class Rectangle(Shape):
#    def __init__(self, x, y, width, height):
#        self.x = x
#        self.y = y
#        self.width = width
#        self.height = height
#
#    def show(self):
#        print(f"Rectangle with upper left corner at ({self.x}, {self.y}), width {self.width} and height {self.height}")
#
#    def save(self, filename):
#        with open(filename, "a") as f:
#            f.write(f"Rectangle {self.x} {self.y} {self.width} {self.height}\n")
#
#    @classmethod
#    def load(cls, filename):
#        rectangles = []
#        with open(filename, "r") as f:
#            lines = f.readlines()
#            for line in lines:
#                data = line.strip().split()
#                if data[0] == "Rectangle":
#                    x = int(data[1])
#                    y = int(data[2])
#                    width = int(data[3])
#                    height = int(data[4])
#                    rectangle = Rectangle(x, y, width, height)
#                    rectangles.append(rectangle)
#        return rectangles
#
#class Circle(Shape):
#    def __init__(self, x, y, radius):
#        self.x = x
#        self.y = y
#        self.radius = radius
#
#    def show(self):
#        print(f"Circle with center at ({self.x}, {self.y}) and radius {self.radius}")
#
#    def save(self, filename):
#        with open(filename, "a") as f:
#            f.write(f"Circle {self.x} {self.y} {self.radius}\n")
#
#    @classmethod
#    def load(cls, filename):
#        circles = []
#        with open(filename, "r") as f:
#            lines = f.readlines()
#            for line in lines:
#                data = line.strip().split()
#                if data[0] == "Circle":
#                    x = int(data[1])
#                    y = int(data[2])
#                    radius = int(data[3])
#                    circle = Circle(x, y, radius)
#                    circles.append(circle)
#        return circles
#
#class Ellipse(Shape):
#    def __init__(self, x, y, width, height):
#        self.x = x
#        self.y = y
#        self.width = width
#        self.height = height
#
#    def show(self):
#        print(f"Ellipse with upper left corner at ({self.x}, {self.y}), width {self.width} and height {self.height}")
#
#    def save(self, filename):
#        with open(filename, "a") as f:
#            f.write(f"Ellipse {self.x} {self.y} {self.width} {self.height}\n")
#
#    @classmethod
#    def load(cls, filename):
#        ellipses = []
#        with open(filename, "r") as f:
#            lines = f.readlines()
#            for line in lines:
#                data = line.strip().split()
#                if data[0] == "Ellipse":
#                    x = int(data[1])
#                    y = int(data[2])
#                    width = int(data[3])
#                    height = int(data[4])
#                    ellipse = Ellipse(x, y, width, height)
#                    ellipses.append(ellipse)
#        return ellipses
#
#shapes = [Square(10, 10, 20), Rectangle(30, 40, 50, 60), Circle(70, 80, 90), Ellipse(100, 200, 150, 100)]
#
#filename = "shapes.txt"
#with open(filename, "w") as f:
#    f.write("")
#
#for shape in shapes:
#    shape.save(filename)

