"""skip"""


def main(size):
    """ sequence """
    for rows in range(-size + 1, size):
        for col in range(-size + 1, size):
            print("%02d" % (size - abs(abs(rows) - abs(col))), end=" ")
        print()


main(int(input()))
