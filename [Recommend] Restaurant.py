'''Restaurant'''


def main():
    '''Restaurant'''
    price = float(input())
    promo = float(input())
    discount = float(input())
    offer = float(input())
    if price + offer >= promo:
        with_pro = (price + offer) * (100 - discount) / 100
    else:
        with_pro = price + offer
    if price >= promo:
        without_pro = price * (100 - discount) / 100
    else:
        without_pro = price
    ans = abs(with_pro - without_pro)
    if without_pro > with_pro:
        print('Yes %.3f' % ans)
    elif with_pro > without_pro:
        print('No %.3f' % ans)
    else:
        print('Yes')


main()
