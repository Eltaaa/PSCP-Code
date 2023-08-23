""" LeftArrow """


def main(width, height):
    """ Arrow """
    
    num = int((height - 1) / 2)
    for rows in range(-num, num + 1):
        print(" " * (abs(rows)), end="")
        print("*" * width)


main(int(input()), int(input()))
