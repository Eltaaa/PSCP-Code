""" sequence iii """


def main(size):
    """ sequence """

    for rows in range(1, size+1):
        for col in range(1, size+1):
            print(col+rows, end=" ")
        print()


main(int(input()))
