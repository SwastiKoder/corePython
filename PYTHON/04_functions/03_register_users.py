def get_input(name):
    print(f"Getting input of {name}")


def validate_input(name):
    print(f"Validating input of {name}")


def save_to_db(name):
    print(f"Adding {name} to DB")


def register_users(name):
    get_input(name)
    validate_input(name)
    save_to_db(name)
    print(f"User {name} registered")


register_users("Swastik")