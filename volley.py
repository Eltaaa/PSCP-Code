""" colley """


def main(string):
    """ volley result """
    apoint, aset = 0, 0
    bpoint, bset = 0, 0
    check = 25
    for i in string:
        if i == "A":
            apoint += 1
        else:
            bpoint += 1

        if aset + bset == 4:
            check = 15

        if apoint >= check and apoint - bpoint >= 2:
            aset += 1
            print("Set %d: A (%d) | B (%d)" % (aset + bset, apoint, bpoint))
            apoint = 0
            bpoint = 0
        elif bpoint >= check and bpoint - apoint >= 2:
            bset += 1
            print("Set %d: A (%d) | B (%d)" % (aset + bset, apoint, bpoint))
            apoint = 0
            bpoint = 0

        if aset >= 3 or bset >= 3:
            break

    # if aset + bset <= 3:

    if aset >= 3:
        print("A won %d:%d set" % (aset, bset))
    elif bset >= 3:
        print("B won %d:%d set" % (bset, aset))
    else:
        print("Set %d: A (%d) | B (%d)" % (aset + bset + 1, apoint, bpoint))
        print("The game has not finished yet.")


main(input())
