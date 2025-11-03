import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)
        self.assertEqual(Calculator.add(-1, -2), -3)
        with self.assertRaises(TypeError):
            Calculator.add(1, "a")
    
    def test_subtract(self):
        self.assertEqual(Calculator.subtract(2, 1), 1)
        self.assertEqual(Calculator.subtract(-1, -1), 0)
        with self.assertRaises(TypeError):
            Calculator.subtract(1, "a")
    
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertEqual(Calculator.multiply(-1, 2), -2)
        with self.assertRaises(TypeError):
            Calculator.multiply(2, "a")
    
    def test_divide(self):
        self.assertEqual(Calculator.divide(4, 2), 2)
        with self.assertRaises(ValueError):
            Calculator.divide(1, 0)
        with self.assertRaises(TypeError):
            Calculator.divide(1, "a")
    
    def test_power(self):
        self.assertEqual(Calculator.power(2, 3), 8)
        with self.assertRaises(TypeError):
            Calculator.power(2, "a")
    
    def test_sqrt(self):
        self.assertEqual(Calculator.sqrt(4), 2)
        with self.assertRaises(ValueError):
            Calculator.sqrt(-1)
        with self.assertRaises(TypeError):
            Calculator.sqrt("a")
    
    def test_log10(self):
        self.assertEqual(Calculator.log10(100), 2)
        with self.assertRaises(ValueError):
            Calculator.log10(0)
        with self.assertRaises(ValueError):
            Calculator.log10(-1)
        with self.assertRaises(TypeError):
            Calculator.log10("a")

if __name__ == '__main__':
    unittest.main()
