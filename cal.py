""" cal """


def main(num):
    """ count how many button were pressed """
    string = ""
    for i in range(1, num + 1):
        string += str(i)
        string += "+"
    # print(string)
    if num == 1:
        print(1)
    else:
        print(len(string))


main(int(input()))
