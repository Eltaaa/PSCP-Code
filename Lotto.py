""" lotto """


def main(win):
    """ dsadsa """
    last2 = input()
    first3 = input()
    first3_2 = input()
    last3 = input()
    last3_2 = input()
    bought = input()
    get = 0

    if win == "000000":
        near1 = '999999'
        near2 = '000001'
    elif win == '999999':
        near1 = '999998'
        near2 = '000000'
    else:
        near1 = str(int(win)-1)
        near2 = str(int(win)+1)

    if bought == win:
        get += 6000000
    if bought[-2:] == last2:
        get += 2000
    if bought[0:3] == first3:
        get += 4000
    if bought[0:3] == first3_2:
        get += 4000
    if bought[-3:] == last3:
        get += 4000
    if bought[-3:] == last3_2:
        get += 4000
    if bought == near1 or bought == near2:
        get += 100000
    print(get)


main(input())
