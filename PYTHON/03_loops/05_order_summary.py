names = ["Swastik" , "Abinash" , "Pradeep" , "Sidhant" , "Aditya"]
amount = [1 , 20 , 30 , 40 , 50]


for name , amounts in zip(names , amount):
    print(f"{name} paid {amounts} for chai")