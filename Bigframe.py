""" big frame """


def main():
    """ das """
    line1 = input().strip()
    length = len(line1)
    line2 = input().strip()
    length = longest(length, line2)
    line3 = input().strip()
    length = longest(length, line3)
    line4 = input().strip()
    length = longest(length, line4)
    line5 = input().strip()
    length = longest(length, line5)

    print("*"*(length+4))
    print("*", line1.ljust(length), "*")
    print("*", line2.ljust(length), "*")
    print("*", line3.ljust(length), "*")
    print("*", line4.ljust(length), "*")
    print("*", line5.ljust(length), "*")
    print("*"*(length+4))


def longest(length, word):
    ''' determine the longest word'''
    if len(word) > length:
        length = len(word)
    return length


main()
