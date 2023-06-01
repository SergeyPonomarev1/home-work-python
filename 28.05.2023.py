# Задание 1
#import unittest
#
#class NumberSet:
#    def __init__(self, numbers):
#        self.numbers = numbers
#
#    def sum(self):
#        return sum(self.numbers)
#
#    def average(self):
#        return sum(self.numbers) / len(self.numbers)
#
#    def maximum(self):
#        return max(self.numbers)
#
#    def minimum(self):
#        return min(self.numbers)
#
#class TestNumberSet(unittest.TestCase):
#    def setUp(self):
#        self.numbers = NumberSet([1, 2, 3, 4, 5])
#
#    def test_sum(self):
#        self.assertEqual(self.numbers.sum(), 15)
#
#    def test_average(self):
#        self.assertEqual(self.numbers.average(), 3)
#
#    def test_maximum(self):
#        self.assertEqual(self.numbers.maximum(), 5)
#
#    def test_minimum(self):
#        self.assertEqual(self.numbers.minimum(), 1)
#
#if __name__ == '__main__':
#    unittest.main()


# Задание 2
#import unittest
#
#class Number:
#    def __init__(self, value):
#        self.value = value
#
#    def set_value(self, value):
#        self.value = value
#
#    def get_value(self):
#        return self.value
#
#    def to_octal(self):
#        return oct(self.value)
#
#    def to_hexadecimal(self):
#        return hex(self.value)
#
#    def to_binary(self):
#        return bin(self.value)
#
#class TestNumber(unittest.TestCase):
#    def setUp(self):
#        self.number = Number(10)
#
#    def test_set_value(self):
#        self.number.set_value(20)
#        self.assertEqual(self.number.get_value(), 20)
#
#    def test_to_octal(self):
#        self.assertEqual(self.number.to_octal(), '0o12')
#
#    def test_to_hexadecimal(self):
#        self.assertEqual(self.number.to_hexadecimal(), '0xa')
#
#    def test_to_binary(self):
#        self.assertEqual(self.number.to_binary(), '0b1010')
#
#if __name__ == '__main__':
#    unittest.main()