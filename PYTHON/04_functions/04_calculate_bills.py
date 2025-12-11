def calculate_bills(cups, price_per_cup):
    return cups * price_per_cup


total_price = 0

for i in range(0, 3):
    cups = int(input("Enter the number of cups : "))
    price_per_cup = int(input("Enter the price of cup : "))
    print(f"Total price for this section is {calculate_bills(cups , price_per_cup)}")
    total_price += calculate_bills(cups, price_per_cup)

print(f"Total price of your order is : {total_price}")
