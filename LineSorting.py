""" sorting """


def main(num):
    """ sorting string by length """
    string = []
    for _ in range(num):
        string.append(input())

    string.sort(key=len)
    for i in string:
        print(i)


main(int(input()))
