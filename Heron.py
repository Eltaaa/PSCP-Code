""" heron """


def main(anum, bnum, cnum):
    """ Triangle Area using Heron's formula """
    snum = (anum + bnum + cnum) / 2
    area = snum*(snum - anum)*(snum - bnum)*(snum - cnum)
    print("%.3f" % (area**0.5))


main(float(input()), float(input()), float(input()))
