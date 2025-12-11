ingredients = ["water", "tea", "black tea"]
ingredients.append("milk")
print(f"Ingredients are : {ingredients}")
ingredients.remove("milk")
print(f"Ingredients are : {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["milk", "tea"]

chai_ingredients.extend(spice_options)
print(f"Chai Ingredients are : {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"Chai Ingredients are : {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"Chai Ingredients are : {chai_ingredients}")
chai_ingredients.reverse()
print(f"Ingredients in reverse : {chai_ingredients}")
chai_ingredients.sort()
print(f"Chai Ingredients in short : {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum Sugar Level : {max(sugar_levels)}")
print(f"Minimum Sugar Level is : {min(sugar_levels)}")

# operator overloading -> a operator have to do work which is not supposed to be done by the operator
base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid Mix : {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong Brew : {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes : {raw_spice_data}")
