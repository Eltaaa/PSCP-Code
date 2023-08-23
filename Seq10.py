""" sequence x """


def main(size):
    """ sequence """
    for rows in range(-size+1, size):
        for col in range(-size+1, size):
            if abs(rows) + abs(col) <  size:
                print('%02d' % (size - (abs(rows)+abs(col))), end=" ")
            else:
                print('  ', end=" ")
        print()


main(int(input()))
