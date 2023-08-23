""" I'm still worthy """


def main(num):
    """ asdasd """
    worth = -1
    for _ in range(num):
        price = float(input())
        gram = float(input())
        if gram/price > worth:  # WORTH
            worth = gram/price
            worthgram = gram
            lowprice = price
        elif gram/price == worth:  # EQUALLY WORTH
            if price < lowprice:
                lowprice = price
                worthgram = gram
    print('%.2f %.2f' % (lowprice, worthgram))


main(int(input()))
