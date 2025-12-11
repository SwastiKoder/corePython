chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai Order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black_tea"
chai_recipe["liquid"] = "milk"
print(f"Chai Recipe : {chai_recipe}")
del chai_recipe["liquid"]
print(f"Chai Recipe : {chai_recipe}")

print(f"Is Sugar in Chai Order ? {"sugar" in chai_order}")

# print(f"Order Details(keys) : {chai_order.keys()}")
# print(f"Order Details(values) : {chai_order.values()}")
# print(f"Order details(items) : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed Item : {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated Chai Recipe : {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai Size : {chai_size}")

chai_note = chai_order.get("note", "No Note")
print(f"Chai Note : {chai_note}")
