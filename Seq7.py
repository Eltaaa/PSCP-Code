""" sequence vii """


def main(size):
    """ sequence """
    for rows in range(-size+1, size):
        for col in range(1, size+1):
            if col == size+1-abs(rows):
                break
            print(col, end=" ")

        print()


main(int(input()))
