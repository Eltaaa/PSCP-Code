""" afdsf """


def main(baht, cap, trade, money):
    """ dsadas """
    bought = money // baht
    current_cap = bought
    while current_cap >= cap and cap > 0:
        getcap = (current_cap // cap)*trade
        remaincap = current_cap % cap
        bought += getcap
        current_cap = remaincap + getcap
    print(bought)


main(int(input()), int(input()), int(input()), int(input()))
