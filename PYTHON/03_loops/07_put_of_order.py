flavours = ["Ginger", "Out of Stock", "Lemon", "Tulsi", "Discontinued", "Tuls"]

for flavour in flavours:
    if flavour == "Out of Stock":
        print(f"Out of Stock Item")
        continue
    elif flavour == "Discontinued":
        print(f"Discontinued Item Found")
        break
    else:
        print(f"{flavour} chai is Ready to Serve")
