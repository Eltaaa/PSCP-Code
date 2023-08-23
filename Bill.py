""" Bill """


def main(food):
    """ aaa """
    price = food
    service_charge = 0.1*food
    if service_charge <= 50:
        service_charge = 50
    elif service_charge >= 1000:
        service_charge = 1000

    price += service_charge
    # vat service
    price *= 1.07

    print('%.2f' % price)


main(int(input()))
