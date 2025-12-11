# def serve_chai():
#     chai_type = "masala" # local scope
#     print(f"Inside function : {chai_type}")

# chai_type = "mint"
# serve_chai()
# print(f"Outside function : {chai_type}")


def chai_counter():
    chai_order = "masala"

    def print_order():
        chai_order = "ginger"
        print(f"Inside inner funtion : {chai_order}")

    print_order()
    print(f"Ouside inner function : {chai_order}")


chai_order = "Tulsi"  # global
chai_counter()
print(f"Global : {chai_order}")
