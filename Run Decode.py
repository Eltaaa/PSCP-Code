""" decoding """


def main(run):
    """ get code"""
    num = ""
    code = ""
    for i in run:
        if i.isnumeric():
            num += i
        elif i.isalpha():
            code += i
            decode(num, code)
            num = ""
            code = ""
    # print()
    # print("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")


def decode(num, alphabet):
    """ translate """
    print(alphabet*int(num), end="")


main(input())
