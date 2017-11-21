import calc
import unittest


class test_calc(unittest.TestCase):
        
    def test_add(self):
        ''' testing addition '''
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(0, 5), 5)
        self.assertEqual(calc.add(-10, 5), -5)
        self.assertEqual(calc.add(0, -5), -5)

    def test_substract(self):
        self.assertEqual(calc.substract(10, 5), 5)
        self.assertEqual(calc.substract(0, 5), -5)
        self.assertEqual(calc.substract(-10, 5), -15)
        self.assertEqual(calc.substract(0, -5), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(0, 5), 0)
        self.assertEqual(calc.multiply(-10, 5), -50)
        self.assertEqual(calc.multiply(2.2, -5), -11)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(5, 5), 1)
        self.assertEqual(calc.divide(-10, 5), -2)
        self.assertEqual(calc.divide(10, -2.5), -4)



if __name__ == "__main__":
    unittest.main()