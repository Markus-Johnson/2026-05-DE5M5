import unittest
from calculator import calculator

class TestOperations(unittest.TestCase):
      def setUp(self):
            self.calc = calculator(8,2)

class TestOperations(unittest.TestCase):
    def test_sum(self):
        calc = calculator (8,2)
        self.assertEqual(calc.get_sum(), 10, "The answer was not 10.")

# Test for the remaining operations

if __name__ == "__main__":
  unittest.main()

def test_sum(self):
        calc = calculator (8,2)
        self.assertEqual(calc.get_subtraction(), 6, "The answer was not 6.")


def test_sum(self):
        calc = calculator (8,2)
        self.assertEqual(calc.get_multiplication(), 16, "The answer was not 16.")

def test_sum(self):
        calc = calculator (8,2)
        self.assertEqual(calc.get_division(), 4, "The answer was not 4.")

