# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's name : {self.name}")


class Labrador(Dog):  # single inheritance
    def sound(self):
        print(f"Labrador woofs")


# Multilevel Inheritance
class Guidedog(Labrador):
    def guide(self):
        print(f"{self.name} Guides the way !")


#multiple inheritance
class Friendly :
    def greet(self):
        print("Friendly...")

class GoldenRetriever(Friendly,Dog):
    def sound(self):
        print("Golden retriever Barks...")

lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = Guidedog("Max")
guide_dog.guide()

golden = GoldenRetriever("Smith")
golden.sound()
golden.greet()
