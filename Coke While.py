""" coke """


def main(price, cap, price2, want):
    """ dsadas """
    realcost = 0
    cnt = 0
    total = 0
    sec_price = price

    while total < want:
        cnt += 1
        total += 1
        realcost += sec_price
        sec_price = price
        if cnt == cap:
            cnt = 0
            sec_price = price2
    print(realcost)


main(int(input()), int(input()), int(input()), int(input()))
