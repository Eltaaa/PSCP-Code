""" Donut """


def main(a_va, b_va, c_va, d_va):
    """ bruh """
    time_purchase = d_va // (b_va + c_va)
    donuts = (d_va // (b_va + c_va)) * (b_va + c_va)
    price = time_purchase * a_va * b_va
    # those remaining
    if d_va % (b_va + c_va) >= b_va:
        donuts += b_va + c_va
        price += a_va * b_va
    else:
        buy_more = d_va - donuts
        donuts += (buy_more)
        price += a_va * (buy_more)
    print("%d %d" % (price, donuts))


main(int(input()), int(input()), int(input()), int(input()))
