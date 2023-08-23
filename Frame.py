""" frame """


def main(txt):
    """ show text in frame """
    print("*"*(len(txt)+2))
    print("*" + txt + "*")
    print("*"*(len(txt)+2))


main(input())
