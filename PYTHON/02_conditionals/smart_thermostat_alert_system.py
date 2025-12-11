device_status = input("Input Device Status : ")
tempereture = float(input("Give the Tempereture in Degree : "))

if device_status == "active":
    if tempereture > 35:
        print(f"Alert!! High Tempereture")
    else:
        print(f"Tempereture Normal")
else:
    print(f"Device is Normal")
