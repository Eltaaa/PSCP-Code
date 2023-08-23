""" N """


def main(size):
    """ letter N """
    for rows in range(size):
        for col in range(size):
            con1 = col == 0
            con2 = col == size-1
            con3 = col == rows
            if con1 or con2 or con3:
                print("*", end="")
            else:
                print(" ", end="")
        print()


main(int(input()))
