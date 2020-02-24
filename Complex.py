import math

class Complex:

    def __init__(self, real, imaginary):
        self.__real = real
        self.__imaginary = imaginary

    @staticmethod
    def polar_complex(mag:float,phase:float):
        return Complex(mag*math.cos(phase), mag*math.sin(phase))

    def get_real(self):
        return self.__real

    def get_imaginary(self):
        return self.__imaginary

    def add(self, other: 'Complex'):
        return Complex(self.get_real() + other.get_real(), self.get_imaginary() + other.get_imaginary())

    def subtract(self, other: 'Complex'):
        return self.add(other.int_mult(-1))

    def mult(self, other: 'Complex'):
        new_complex = Complex(self.get_real() * other.get_real() - self.get_imaginary() * other.get_imaginary(),
                               self.get_real() * other.get_imaginary() + self.get_imaginary() * other.get_real())
        return new_complex

    def int_mult(self, number: int):
        return Complex(self.get_real() * number, self.get_imaginary() * number)

    def raise_to_int(self, number: int):
        mag = self.get_magnitude()
        phase = self.get_phase()

        mag  **= number
        phase *= number

        return Complex.polar_complex(mag,phase)

    def raise_float_to_complex(self, number:float):
        mag = number**self.__real
        phase = self.__imaginary()*math.log(number)

        return Complex.polar_complex(mag,phase)

    def raise_complex(self,other:'Complex'):
        first_complex_mag = self.get_magnitude()
        first_complex_phase = self.get_phase()

        new_complex_real = other.__real*math.log(first_complex_mag) - first_complex_phase * other.__imaginary
        new_complex_imaginary = other.__imaginary*math.log(first_complex_mag) + first_complex_phase*other.__real
        new_complex = Complex(new_complex_real,new_complex_imaginary)

        return new_complex.raise_float_to_complex(math.e)

    def get_magnitude(self):
        return math.sqrt(self.__real**2+self.__imaginary**2)

    def get_phase(self):
        return math.atan2(self.__real,self.__imaginary)
