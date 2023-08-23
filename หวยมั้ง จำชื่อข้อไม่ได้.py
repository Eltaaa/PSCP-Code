""" asdsadsa """


def main():
    """ dasdas """
    firstprize = input()
    twosuffix = input()
    prefix1 = input()
    prefix2 = input()
    suffix1 = input()
    suffix2 = input()

    gambling = input()
    prize = 0
    prize += winning(gambling, firstprize)
    prize += lastwo(gambling, twosuffix)
    prize += threeprefix(gambling, prefix1, prefix2)
    prize += threesuffix(gambling, suffix1, suffix2)
    print(prize)


def winning(gambling, firstprize):
    """ winning firstprize or neighbor """
    money = 0
    if firstprize != "000000" and firstprize != "999999":
        neighbour1 = "%06d" % (int(firstprize) + 1)
        neighbour2 = "%06d" % (int(firstprize) - 1)
    elif firstprize == "000000":
        neighbour1 = "000001"
        neighbour2 = "999999"
    elif firstprize == "999999":
        neighbour1 = "000000"
        neighbour2 = "999998"
    if gambling == firstprize:
        money += 6000000
    elif gambling == neighbour1 or gambling == neighbour2:
        money += 100000

    return money


def lastwo(gambling, num):
    """ check for last two suffix """
    money = 0
    if gambling[-2:] == num:
        money += 2000
    return money


def threeprefix(gambling, prefix1, prefix2):
    """ check for 3 prefix """
    # what if 3 prefixs are the same number ?
    money = 0
    if gambling[0:3] == prefix1:
        money += 4000
    if gambling[0:3] == prefix2:
        money += 4000
    return money


def threesuffix(gambling, suffix1, suffix2):
    """ check three suffix """
    money = 0
    if gambling[-3:] == suffix1:
        money += 4000
    if gambling[-3:] == suffix2:
        money += 4000
    return money


main()
