# Задание 1
#class Fraction:
#
#    count = 0
#
#    def __init__(self, numerator, denominator):
#        self.numerator = numerator
#        self.denominator = denominator
#        Fraction.count += 1
#
#    def show(self):
#        print(f"{self.numerator}/{self.denominator}")
#
#    @staticmethod
#    def get_count():
#        return Fraction.count
#
#f1 = Fraction(1, 2)
#f2 = Fraction(3, 4)
#f3 = Fraction(5, 6)
#
#print(Fraction.get_count())  # выведет 3, так как созданы три объекта класса "Дробь"

# Задание 2
#class TemperatureConverter:
#
#    count = 0
#
#    @staticmethod
#    def celsius_to_fahrenheit(celsius):
#        TemperatureConverter.count += 1
#        return (celsius * 9/5) + 32
#
#    @staticmethod
#    def fahrenheit_to_celsius(fahrenheit):
#        TemperatureConverter.count += 1
#        return (fahrenheit - 32) * 5/9
#
#    @staticmethod
#    def get_count():
#        return TemperatureConverter.count
#
#print(TemperatureConverter.celsius_to_fahrenheit(0))  # выводит 32.0
#print(TemperatureConverter.fahrenheit_to_celsius(32))  # выводит 0.0
#print(TemperatureConverter.get_count())  # выводит 2, так как два метода конвертирования были вызваны

# Задание 3
#class UnitConverter:
#
#    @staticmethod
#    def meters_to_feet(meters):
#        return meters / 0.3048
#
#    @staticmethod
#    def feet_to_meters(feet):
#        return feet * 0.3048
#
#print(UnitConverter.meters_to_feet(10))  
#print(UnitConverter.feet_to_meters(32.80839895013123))

