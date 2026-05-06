# ── Call the functions ──────────────────────────────────────────
class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        def get_sum(self):
            return self.a + self.b
        
        #Add the methods for subtration, division and multiplication 

        myCalc = calculator (a=3, b=5)
        print(myCalc.get_sum())

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Methods sit outside __init__ but inside the class
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

# This sits outside the class entirely
myCalc = calculator(a=3, b=5)
print(myCalc.get_sum())
print(myCalc.get_subtraction())
print(myCalc.get_multiplication())
print(myCalc.get_division())

if __name__ == "__main__":
    myCalc = calculator(a=3, b=5)
    print(myCalc.get_sum())