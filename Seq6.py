""" sequence vi """


def main(size):
    """ sequence """
    for rows in range(1, size+1):
        for col in range(1, size+1):
            print(col, end=" ")
            if col == rows:
                break
        print()


main(int(input()))
