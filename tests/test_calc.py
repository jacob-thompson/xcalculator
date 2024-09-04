import unittest

from sympy import sympify

class TestCalc(unittest.TestCase):
    def test_addition_works(self):
        test1 = sympify("3+9", evaluate=True)
        test2 = sympify("100+45", evaluate=True)
        test3 = sympify("15250 + 1750", evaluate=True)

        assert test1 == 12
        assert test2 == 145
        assert test3 == 17000

    def test_subtraction_works(self):
        test1 = sympify("24-4", evaluate=True)
        test2 = sympify("1000 - 245", evaluate=True)
        test3 = sympify("15250-1750", evaluate=True)

        assert test1 == 20
        assert test2 == 755
        assert test3 == 13500

    def test_multiplication_works(self):
        test1 = sympify("12 * 3", evaluate=True)
        test2 = sympify("1000 * 42", evaluate=True)
        test3 = sympify("15000*4", evaluate=True)

        assert test1 == 36
        assert test2 == 42000
        assert test3 == 60000

    def test_division_works(self):
        test1 = sympify("9/3", evaluate=True)
        test2 = sympify("100/5", evaluate=True)
        test3 = sympify("1800 / 60", evaluate=True)

        assert float(test1) == 3
        assert float(test2) == 20
        assert float(test3) == 30

if __name__ == '__main__':
    unittest.main()