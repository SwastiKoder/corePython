# def local_chai():
#     yield "Masala Chai"
#     yield "Elaichi Chai"


# def imported_chai():
#     yield "Oolang"
#     yield "Matcha"


# def full_menu():
#     yield from local_chai()
#     yield from imported_chai()

# for chai in full_menu():
#     print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting For Order"
    except:
        print("Stall Closed . No more Chai")

chai = chai_stall()
print(next(chai_stall()))
chai.close() #cleanup
