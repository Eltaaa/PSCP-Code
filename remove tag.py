""" html tag remove """


def main(string):
    """ remove html tag return only string """
    while "<" in string:
        ind1 = string.index("<")
        ind2 = string.index(">")
        tag = string[ind1:ind2 + 1]
        string = string.replace(tag, " ")
    lst = string.split()
    print(lst)


main(input())
