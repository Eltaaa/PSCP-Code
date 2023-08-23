""" diamon """


def main(num):
    """ dsadsa """
    size = int((num-1)/2)

    for rows in range(size, -size-1, -1):
        for col in range(-size, size + 1):
            con1 = rows == 0
            con2 = abs(rows) + abs(col) == size
            if con1 or con2:
                print('*', end="")
            else:
                print(" ", end="")
        print()


main(int(input()))
