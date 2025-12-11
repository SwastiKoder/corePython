def chai_flavor(flavor="ginger"):
    """ "Return the flavor of chai."""
    chai = "ginger"
    return flavor


print(chai_flavor.__doc__)  # it gives the very first line
print(chai_flavor.__name__)


def generate_bill(chai=0, samosa=0):
    """
    Docstring for generate_bill

    :param chai: Number of chai cups 10 each
    :param samosa: Number of samosa 15 each
    :return total price and thank you message
    """
    total = 10 * chai + 15 * samosa
    print(total , "Thank You ! Visit Again")

print(generate_bill.__doc__)
generate_bill(5,10)