chai_type = "Ginger"
customer_name = "Swagatika"
print(f"Chai type for {customer_name} is : {chai_type}")

chai_description = "Aromatic and Bold"
print(f"First Word : {chai_description[: 8]}")
print(f"Last Word : {chai_description[8 :]}")
print(f"Reverse String : {chai_description[::-1]}")

label_text = "Chai Spècial"
encoded_label = label_text.encode("utf-8")
print(f"Not encoded label : {label_text}")
print(f"Encoded Label : {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label : {decoded_label}")