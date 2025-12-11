is_boiling = True
stri_count = 5
total_actions = is_boiling + stri_count  # upcasting
print(f"Total actions is : {total_actions}")

milk_present = None
print(f"Is there Milk ? {bool(milk_present)}")

water_hot = True
tea_added = False
can_serve = water_hot and tea_added
print(f"Can served ? {can_serve}")