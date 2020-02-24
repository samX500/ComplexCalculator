from Complex import Complex


def run_all_test():
    test_addition()
    test_get_magnitude()
    test_get_phase()
    test_multiplication()
    test_raise_complex()
    test_raise_float_to_complex()
    test_raise_to_int()
    test_subtraction()


def test_addition():
    print('began running test_addition')
    complex1 = Complex(5, 4)
    complex2 = Complex(3, 6)
    complex_add = complex1.add(complex2)
    assert complex_add.get_real() == 8, 'Should be 8, is ' + str(complex_add.get_real())
    assert complex_add.get_imaginary() == 10, 'Should be 10, is ' + str(complex_add.get_imaginary())

    complex1 = Complex(-5, 4)
    complex2 = Complex(3, 6)
    complex_add = complex1.add(complex2)
    assert complex_add.get_real() == -2, 'Should be -2, is ' + str(complex_add.get_real())
    assert complex_add.get_imaginary() == 10, 'Should be 10, is ' + str(complex_add.get_imaginary())

    complex1 = Complex(5, -4)
    complex2 = Complex(3, 6)
    complex_add = complex1.add(complex2)
    assert complex_add.get_real() == 8, 'Should be 8, is ' + str(complex_add.get_real())
    assert complex_add.get_imaginary() == 2, 'Should be 2, is ' + str(complex_add.get_imaginary())

    complex1 = Complex(-5, -4)
    complex2 = Complex(3, 6)
    complex_add = complex1.add(complex2)
    assert complex_add.get_real() == -2, 'Should be -2, is ' + str(complex_add.get_real())
    assert complex_add.get_imaginary() == 2, 'Should be 2, is ' + str(complex_add.get_imaginary())

    complex1 = Complex(5, 4)
    complex2 = Complex(-3, 6)
    complex_add = complex1.add(complex2)
    assert complex_add.get_real() == 2, 'Should be 2, is ' + str(complex_add.get_real())
    assert complex_add.get_imaginary() == 10, 'Should be 10, is ' + str(complex_add.get_imaginary())

    complex1 = Complex(5, 4)
    complex2 = Complex(3, -6)
    complex_add = complex1.add(complex2)
    assert complex_add.get_real() == 8, 'Should be 8, is ' + str(complex_add.get_real())
    assert complex_add.get_imaginary() == -2, 'Should be -2, is ' + str(complex_add.get_imaginary())

    complex1 = Complex(5, 4)
    complex2 = Complex(-3, -6)
    complex_add = complex1.add(complex2)
    assert complex_add.get_real() == 2, 'Should be 2, is ' + str(complex_add.get_real())
    assert complex_add.get_imaginary() == -2, 'Should be -2, is ' + str(complex_add.get_imaginary())

    print('Finished running test_addition')

def test_subtraction():

    print('Began running test_subtraction')
    complex1 = Complex(5,4)
    complex2 = Complex(3,6)
    complex_negate  = complex1.subtract(complex2)
    assert complex_negate.get_real() == 2, 'Should be 2, is ' + str(complex_negate.get_real())
    assert complex_negate.get_imaginary() == -2 , 'Should be -2, is ' +complex_negate.get_imaginary()

    complex1 = Complex(-5, 4)
    complex2 = Complex(3, 6)
    complex_negate = complex1.subtract(complex2)
    assert complex_negate.get_real() == -8, 'Should be -8, is ' + str(complex_negate.get_real())
    assert complex_negate.get_imaginary() == -2, 'Should be -2, is ' + str(complex_negate.get_imaginary())

    complex1 = Complex(5, -4)
    complex2 = Complex(3, 6)
    complex_negate = complex1.subtract(complex2)
    assert complex_negate.get_real() == 2, 'Should be 2, is ' + str(complex_negate.get_real())
    assert complex_negate.get_imaginary() == -10, 'Should be -10, is ' + str(complex_negate.get_imaginary())

    complex1 = Complex(-5, -4)
    complex2 = Complex(3, 6)
    complex_negate = complex1.subtract(complex2)
    assert complex_negate.get_real() == -8, 'Should be -8, is ' + str(complex_negate.get_real())
    assert complex_negate.get_imaginary() == -10, 'Should be -10, is ' + str(complex_negate.get_imaginary())

    complex1 = Complex(5, 4)
    complex2 = Complex(-3, 6)
    complex_negate = complex1.subtract(complex2)
    assert complex_negate.get_real() == 8, 'Should be 8, is ' + str(complex_negate.get_real())
    assert complex_negate.get_imaginary() == -2, 'Should be -2, is ' + str(complex_negate.get_imaginary())

    complex1 = Complex(5, 4)
    complex2 = Complex(3, -6)
    complex_negate = complex1.subtract(complex2)
    assert complex_negate.get_real() == 2, 'Should be 2, is ' + str(complex_negate.get_real())
    assert complex_negate.get_imaginary() == 10, 'Should be 10, is ' + str(complex_negate.get_imaginary())

    complex1 = Complex(5, 4)
    complex2 = Complex(-3, -6)
    complex_negate = complex1.subtract(complex2)
    assert complex_negate.get_real() == 8, 'Should be 8, is ' + str(complex_negate.get_real())
    assert complex_negate.get_imaginary() == 10, 'Should be 10, is ' + str(complex_negate.get_imaginary())

    print('Finished running test_subtraction')

def test_multiplication():

    print('Began running test_multiplication')
    complex1 = Complex(5,4)
    complex2 = Complex(3,6)
    complex_mult = complex1.mult(complex2)
    assert complex_mult.get_real() == -9, 'Should be -9, is ' +complex_mult.get_real()
    assert complex_mult.get_imaginary() == 42, 'Should be 42, is '+complex_mult.get_imaginary()

    complex1 = Complex(-5, 4)
    complex2 = Complex(3, 6)
    complex_mult = complex1.mult(complex2)
    assert complex_mult.get_real() == -39, 'Should be -39, is ' + str(complex_mult.get_real())
    assert complex_mult.get_imaginary() == -18, 'Should be -18, is ' + str(complex_mult.get_imaginary())

    complex1 = Complex(5, -4)
    complex2 = Complex(3, 6)
    complex_mult = complex1.mult(complex2)
    assert complex_mult.get_real() == 39, 'Should be 39, is ' + str(complex_mult.get_real())
    assert complex_mult.get_imaginary() == 18, 'Should be 18, is ' + str(complex_mult.get_imaginary())

    complex1 = Complex(-5, -4)
    complex2 = Complex(3, 6)
    complex_mult = complex1.mult(complex2)
    assert complex_mult.get_real() == 9, 'Should be 9, is ' + str(complex_mult.get_real())
    assert complex_mult.get_imaginary() == -42, 'Should be -42, is ' + str(complex_mult.get_imaginary())

    complex1 = Complex(5, 4)
    complex2 = Complex(-3, 6)
    complex_mult = complex1.mult(complex2)
    assert complex_mult.get_real() == -39, 'Should be -9, is ' + str(complex_mult.get_real())
    assert complex_mult.get_imaginary() == 18, 'Should be 42, is ' + str(complex_mult.get_imaginary())

    complex1 = Complex(5, 4)
    complex2 = Complex(3, -6)
    complex_mult = complex1.mult(complex2)
    assert complex_mult.get_real() == 39, 'Should be 39, is ' + str(complex_mult.get_real())
    assert complex_mult.get_imaginary() == -18, 'Should be -18, is ' + str(complex_mult.get_imaginary())

    complex1 = Complex(5, 4)
    complex2 = Complex(-3, -6)
    complex_mult = complex1.mult(complex2)
    assert complex_mult.get_real() == 9, 'Should be 9, is ' + str(complex_mult.get_real())
    assert complex_mult.get_imaginary() == -42, 'Should be -42, is ' + str(complex_mult.get_imaginary())

    print('Finshed running test_multiplication')

def test_raise_to_int():
    complex1 = Complex(5,4)
    exponent = 3
    complex_raised = complex1.raise_to_int(exponent)
    assert complex_raised.get_real() == -115, 'Should be -115, is ' + str(complex_raised.get_real())
    assert complex_raised.get_imaginary() == 236, 'Should be 236, is ' + str(complex_raised.get_imaginary())

    complex1 = Complex(-5, 4)
    exponent = 3
    complex_raised = complex1.raise_to_int(exponent)
    assert complex_raised.get_real() == 115, 'Should be 115, is ' + str(complex_raised.get_real())
    assert complex_raised.get_imaginary() == 236, 'Should be 236, is ' + str(complex_raised.get_imaginary())

    complex1 = Complex(5, -4)
    exponent = 3
    complex_raised = complex1.raise_to_int(exponent)
    assert complex_raised.get_real() == -115, 'Should be -115, is ' + str(complex_raised.get_real())
    assert complex_raised.get_imaginary() == -236, 'Should be -236, is ' + str(complex_raised.get_imaginary())

    complex1 = Complex(-5, -4)
    exponent = 3
    complex_raised = complex1.raise_to_int(exponent)
    assert complex_raised.get_real() == 115, 'Should be 115, is ' + str(complex_raised.get_real())
    assert complex_raised.get_imaginary() == -236, 'Should be -236, is ' + str(complex_raised.get_imaginary())

    complex1 = Complex(5, 4)
    exponent = -3
    complex_raised = complex1.raise_to_int(exponent)
    assert complex_raised.get_real() == 1/-115, 'Should be 1/-115, is ' + str(complex_raised.get_real())
    assert complex_raised.get_imaginary() == 1/236, 'Should be 1/236, is ' + str(complex_raised.get_imaginary())


def test_raise_float_to_complex():
    print('TODO')


def test_raise_complex():
    print('TODO')


def test_get_magnitude():
    print('TODO')


def test_get_phase():
    print('TODO')


if __name__ == '__main__':
    run_all_test()
