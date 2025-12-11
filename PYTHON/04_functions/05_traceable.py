def add_vat(price, rate):
    return price * (100 + rate) / 100


prices = [150, 250, 90]

for price in prices:
    vat = add_vat(price, 10)
    print(f"Your total bill is : {vat}")
