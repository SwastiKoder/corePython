class ChaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type} chai"


chai = ChaiOrder("Masala", 200)
print(chai.summary())

chai_two = ChaiOrder("Ginger", 150)
print(chai_two.summary())
