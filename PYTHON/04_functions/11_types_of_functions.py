total_chai = 10


# not recommended
def impure_chai(cups):  # accessing the global variable . Impure functions
    global total_chai
    total_chai += cups


def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups Poured"
    return pour_chai(n - 1)


print(pour_chai(4))

chai_types = ["light" , "kadak" , "ginger" , "kadak"]
strong_chai = list(filter(lambda chai : chai == "kadak" , chai_types))
print(strong_chai)
