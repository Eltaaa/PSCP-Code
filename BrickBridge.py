""" Brick bridge """


def main(a_amount, b_amount, length):
    """ bridge """
    # Can't reach
    if a_amount + 5*b_amount < length or a_amount < length % 5:
        print(-1)
        return

    if b_amount*5 >= length:
        b_amount = length//5

    a_used = length - b_amount * 5
    print(a_used)


main(int(input()), int(input()), int(input()))
