daily_sales = [15, 20, 30, 55, 14, 25]

total_cups = sum(price for price in daily_sales if price > 15)

print(total_cups)
