""" one for all """


def main(num):
    """ das """
    string = ""
    for i in range(1, num + 1):
        name = input()
        string += name

        if i == num:
            string += '_%s' % num
        elif i % 2 == 0:
            string += "-"*i
        elif i % 2 == 1:
            string += "*"*i
    print(string)


main(int(input()))
