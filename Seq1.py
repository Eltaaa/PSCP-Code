""" sequence i """


def main(size):
    """ sequence """

    for _ in range(1, size+1):
        for col in range(1, size+1):
            print(col, end=" ")
        print()


main(int(input()))
