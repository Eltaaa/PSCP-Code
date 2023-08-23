""" bagar """


def main(leftbun, rightbun):
    """ hamburger """
    print("|"*leftbun + "*" * (2*(leftbun + rightbun)) + "|"*rightbun)


main(int(input()), int(input()))
