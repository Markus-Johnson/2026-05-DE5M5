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

myCalc = Calculator(a=3, b=5)
print(myCalc.get_sum())
print(myCalc.get_subtraction())
print(myCalc.get_multiplication())
print(myCalc.get_division())