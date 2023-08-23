""" sequence viii """


def main(size):
    """ sequence """
    for rows in range(1, size + 1):
        num = 1
        for col in range(1, size + 1):
            if col > size-rows:
                print('%02d' % num, end=" ")
                num += 1
            else:
                print("  ", end=" ")
        print()


main(int(input()))
