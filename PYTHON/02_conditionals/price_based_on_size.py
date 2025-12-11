size = input("Enter the size of your Chai : ").lower()

if size == "small":
    print(f"Your cup price is 10 for {size} cup")
elif size == "medium":
    print(f"Your cup price is 15 for {size} cup")
elif size == "large":
    print(f"Your cup price is 20 for {size} cup")
else:
    print(f"Oops!! Unknown Cup Size")
