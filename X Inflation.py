'''Inflation'''


def main():
    '''Inflation'''
    money = float(input())
    year = int(input())
    money = int(money*100)
    for _ in range(year):
        digit = money*381//10000
        money = money + digit
    digit = str(money)[-2:]
    money = str(money)[:-2]
    if money == "":
        money = 0
    print('%d.%02d' % (int(money), int(digit)))


main()
