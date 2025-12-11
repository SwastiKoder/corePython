masala_spices = ("cardamom" , "cloves" , "cinnamon")

(spices1 , spices2 , spices3) = masala_spices

print(f"Main Masala Spices : {spices1} , {spices2} , {spices3}")

ginger_ratio , cardamom_ratio = 2 , 1
print(f"Ratio for G : {ginger_ratio} , {cardamom_ratio}")

ginger_ratio , cardamom_ratio = cardamom_ratio , ginger_ratio
print(f"Updated ratio for G : {ginger_ratio} , {cardamom_ratio}")

#membership

print(f"Is there Ginger in masala_spices ? {"ginger" in masala_spices}")
print(f"Is there Cinnamon in masala_spices ? {"cinnamon" in masala_spices}")