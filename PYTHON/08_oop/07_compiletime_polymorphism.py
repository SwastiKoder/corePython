class Calculator:
    def add(self , *args):
        print(f"The sum of the number('s) is {sum(args)}")

calc = Calculator()
calc.add(5 , 6)
calc.add(5 , -1 , 6)
calc.add(-1 , -2 , -3)