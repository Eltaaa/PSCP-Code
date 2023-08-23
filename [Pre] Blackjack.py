""" blackjack """


def main(amount):
    """ hands """
    lst = []
    lst_a = []
    for _ in range(amount):
        card = input()

        if card in "jkqJKQ":
            card = 10
            lst.append(card)
        elif card in "Aa":
            lst_a.append("A")
        else:  # number
            lst.append(int(card))

    while len(lst_a) > 0:

        lst_a.remove("A")

        if sum(lst) + 11 > 21:
            lst.append(1)
        elif sum(lst) == 10 and len(lst_a) == 1:
            lst.append(1)
        else:
            lst.append(11)

    print(sum(lst))


main(int(input()))
