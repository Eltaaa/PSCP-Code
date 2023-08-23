""" sequence ix """


def main(size):
    """ sequence """

    for rows in range(1, size + 1):
        for col in range(-size + 1, size):
            if rows > abs(col):
                print('%02d' % (abs(abs(col) - abs(rows))), end=" ")
                # print('00', end=" ")
            else:
                print("  ", end=" ")
        print()


main(int(input()))
