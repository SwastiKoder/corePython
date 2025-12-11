class Chai:
    origin = "India"


print(Chai.origin)

Chai.is_hot = True

print(Chai.is_hot)

masala = Chai()
masala.is_hot = False

print(f"{masala.origin}")
print(f"{masala.is_hot}")

print(f"Class : ", Chai.is_hot)

masala.flavor = "masala"
print(masala.flavor) #it doesnot create a attribute inside Chai

# print(Chai.flavor)
