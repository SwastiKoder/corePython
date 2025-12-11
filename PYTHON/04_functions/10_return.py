# def make_chai():
#     return "Here is your masala chai"

# return_value = make_chai()
# print(return_value)

def chai_wala():
    pass

print(chai_wala())

def chai_wala(cups):
    if cups == 0:
        return "Sorry Chai is Over"
    return "Chai is ready"

print(chai_wala(0))
print(chai_wala(3))

def chai_report():
    return 100 , 20 , 10 #sold , cups

sold , cups , _ = chai_report()
print("Sold : " , sold , " Cups : " , cups)

