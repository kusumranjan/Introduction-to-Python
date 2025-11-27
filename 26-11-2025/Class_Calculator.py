class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
        try:
           return a/b
        except ZeroDivisionError:
           return "Error: division by zero"

calc = calculator()

print(calc.add(1,2))
print(calc.sub(2,3))
print(calc.mul(3,4))
print(calc.div(3,4))
