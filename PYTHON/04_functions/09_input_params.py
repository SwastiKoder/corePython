# chai = "Ginger chai"

# def prepare_chai(chai):
#     print("Preparing " , chai)

# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]


def edit_chai(chai):
    chai[1] = 4


edit_chai(chai)
print(chai)


def making_chai(tea, milk, sugar):
    print(tea, milk, sugar)


making_chai("Darjeeling", "No", "Low")  # positional
making_chai(tea="Green", sugar="high", milk="ofcourse") #keywords

def special_chai(*ingredients , **extras):
    print("Ingredients" , ingredients)
    print("Extras" , extras)

special_chai("Ginger" , "Cinamon" , sweeteener = "Honey" , foam = "Yes")    
