from datetime import datetime

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_subtraction(self):
        return self.a - self.b

    def get_multiplication(self):
        return self.a * self.b

    def get_division(self):
        if self.b == 0:
            return "Cannot divide by zero"
        return self.a / self.b

    def get_prod(self):
        return self.a * self.b

    def calculate_borrow_days(self, checkout_date, return_date):
        checkout = datetime.strptime(checkout_date, "%d/%m/%Y")
        returned = datetime.strptime(return_date, "%d/%m/%Y")
        days = (returned - checkout).days
        return days

    def is_late(self, checkout_date, return_date, allowed_days=14):
        days = self.calculate_borrow_days(checkout_date, return_date)
        return days > allowed_days

import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):
    def test_sum(self):
        calc = Calculator(8, 2)
        self.assertEqual(calc.get_sum(), 10, "The answer was not 10.")

    def test_subtraction(self):
        calc = Calculator(8, 2)
        self.assertEqual(calc.get_subtraction(), 6, "The answer was not 6.")

    def test_multiplication(self):
        calc = Calculator(8, 2)
        self.assertEqual(calc.get_multiplication(), 16, "The answer was not 16.")

    def test_division(self):
        calc = Calculator(8, 2)
        self.assertEqual(calc.get_division(), 4, "The answer was not 4.")

    def test_division_by_zero(self):
        calc = Calculator(8, 0)
        self.assertEqual(calc.get_division(), "Cannot divide by zero", "Division by zero not handled.")

    # ── Library borrow day tests ────────────────────────────────
    def test_borrow_days(self):
        calc = Calculator(0, 0)
        result = calc.calculate_borrow_days("20/02/2023", "25/02/2023")
        self.assertEqual(result, 5, "Borrow days should be 5.")

    def test_borrow_days_two_weeks(self):
        calc = Calculator(0, 0)
        result = calc.calculate_borrow_days("01/04/2023", "15/04/2023")
        self.assertEqual(result, 14, "Borrow days should be 14.")

    def test_is_late(self):
        calc = Calculator(0, 0)
        result = calc.is_late("01/04/2023", "20/04/2023")
        self.assertTrue(result, "Book should be flagged as late.")

    def test_is_not_late(self):
        calc = Calculator(0, 0)
        result = calc.is_late("01/04/2023", "10/04/2023")
        self.assertFalse(result, "Book should not be flagged as late.")

if __name__ == "__main__":
    unittest.main()