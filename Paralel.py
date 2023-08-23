""" Parallelogram """


def main(text):
    """ Parallelogram """
    for rows in range(1, len(text)*2):
        print(" "*(len(text)-rows), end="")
        if rows <= len(text):
            print(text[:rows])
        else:
            print(text[rows-len(text):])

main(input())
