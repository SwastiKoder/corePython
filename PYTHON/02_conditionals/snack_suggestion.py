snack = input("Enter your preferred Snack : ").lower()

print(f"Preferred Snack : {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Order Confirmed and Great Choice . We will serve you {snack}")
else:
    print(f"Sory we are only serve Cookies or Samosa with Tea")
