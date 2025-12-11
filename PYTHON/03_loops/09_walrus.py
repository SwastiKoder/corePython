value = 13

if remainder := value % 5:
    print(f"Not divisible , remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size : ").lower()) in available_sizes:
    print(f"Your chai cup {requested_size} size is on the way")
else:
    print(f"Not available")


flavors = ["masala" , "lemon" , "ginger" , "mint"]

print("Available flavors : " , flavors)

while (flavor := input("Enter your flavor : ").lower()) not in flavors:
    print(f"Not in the list")

print(f"You choose {flavor} chai")    
