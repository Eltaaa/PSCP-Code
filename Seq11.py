""" sequence xi """


def main(size):
    """ sequence """
    size -= 1
    for rows in range(-size, size + 1):
        for col in range(-size, size + 1):
            print("%02d" % (size + 1 - max(abs(rows), abs(col))), end=" ")
        print()


main(int(input()))
