class Chai:
    tempereture = "hot"
    strength = "strong"


cutting = Chai()
print(cutting.strength)

cutting.strength = "mild"
cutting.size = "small"

print(f"After changing : {cutting.strength}")
print(f"Directly look to the class : {Chai.strength}")
print(f"The size of the cup : {cutting.size}")

del cutting.strength
print(cutting.strength)
del cutting.size
# print(cutting.size) #it can not print anything because the class has no attributes it is the attribut of object cutting
