""" align led sign """


def main(size, alignment, txt):
    """ print aligned txt """
    if alignment == "left":
        print(txt.ljust(size))
    elif alignment == "center":
        txt2 = txt.center(size)
        spacecount = txt2.count(" ")
        if spacecount % 2 == 1:
            print(" "*int((spacecount+1)/2), end="")
            print(txt, end="")
            print(" "*int((spacecount-1)/2), end="")
        else:
            print(txt2)
    else:
        print(txt.rjust(size))


main(int(input()), input().lower(), input())
