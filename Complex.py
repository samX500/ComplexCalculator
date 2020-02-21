class Complex:

    def __init__(self, real, imaginary):
        self.__real = real
        self.__imaginary = imaginary

    def get_real(self):
        return self.__real

    def get_imaginary(self):
        return self.__imaginary

    def add(self, other):
        return Complex(self.get_real() + other.get_real(), self.get_imaginary() + other.get_imaginary())

    def subtract(self, other):
        return self.add(other.int_mult(-1))

    def mult(self, other):
        return Complex(self.get_real() * other.get_real() - self.get_imaginary() * other.get_imaginary(),
                       self.get_real() * other.get_imaginary() + self.get_imaginary() * other.get_real())

    def int_mult(self, number):
        return Complex(self.get_real() * number, self.get_imaginary() * number)
