import argparse
import math

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

    def get_square_root(self):
        if self.a < 0:
            return "Cannot square root a negative number"
        return math.sqrt(self.a)

# ── Argparse setup ──────────────────────────────────────────────
parser = argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("--square_root", type=float, help="Find the square root of a number")
args = parser.parse_args()

# ── Run the calculator ──────────────────────────────────────────
if args.square_root is not None:
    myCalc = Calculator(a=args.square_root, b=0)
    print(f"Square root of {args.square_root} is {myCalc.get_square_root()}")
else:
    myCalc = Calculator(a=3, b=5)
    print("Sum:", myCalc.get_sum())
    print("Subtraction:", myCalc.get_subtraction())
    print("Multiplication:", myCalc.get_multiplication())
    print("Division:", myCalc.get_division())