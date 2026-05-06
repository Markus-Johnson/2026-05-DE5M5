from calculator import calculator

# myCalcV2 = calculator(2, 9)

# print(myCalcV2.get_prod())


from calculator import calculator

class SciCalc(Calculator):
    def get_exp(self):
        return self.a ** self.b

# These two lines sit outside the class
mysciCalc = SciCalc(a=2, b=3)
print(mysciCalc.get_exp())