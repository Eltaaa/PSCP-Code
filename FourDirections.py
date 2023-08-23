""" four direction """


def main(string):
    """ arrow key """
    # LINE 1
    for i in string:
        print("  *  ", end=" ")
    print()

    # LINE 2
    for i in string:
        line2(i)
    print()

    # LINE 3
    for i in string:
        line3(i)
    print()

    # LINE 4
    for i in string:
        line4(i)
    print()

    # LINE 5
    for i in string:
        print("  *  ", end=" ")
    print()


def line2(alphabet):
    '''line 2'''
    if alphabet == 'U':
        print(" *** ", end=" ")
    elif alphabet == 'D':
        print("  *  ", end=" ")
    elif alphabet == 'L':
        print(" *   ", end=" ")
    else:
        print("   * ", end=" ")


def line3(alphabet):
    ''' line3 '''
    if alphabet == 'U' or alphabet == 'D':
        print("* * *", end=" ")
    else:
        print("*****", end=" ")


def line4(alphabet):
    '''' line4'''
    if alphabet == 'D':
        print(" *** ", end=" ")
    elif alphabet == 'U':
        print("  *  ", end=" ")
    elif alphabet == 'R':
        print("   * ", end=" ")
    else:
        print(" *   ", end=" ")


main(input())
