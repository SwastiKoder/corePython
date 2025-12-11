def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print(f"The updated chai type is : {chai_type}")


update_order()    