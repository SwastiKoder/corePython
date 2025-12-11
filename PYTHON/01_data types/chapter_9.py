essential_spices = {"cardamom" , "ginger" , "cinnamon"}
optional_spices = {"cloves" , "ginger" , "black pepper"}

all_spices = essential_spices | optional_spices #UNION
print(f"All Spices : {all_spices}")

common_spices = essential_spices & optional_spices #INTERSECTION
print(f"Common Spices : {common_spices}")

only_in_essentialspices = all_spices - optional_spices
print(f"Only in Optional Spices : {only_in_essentialspices}")

print(f"Is 'cloves' in Essential Spices ? {'cloves' in essential_spices}")