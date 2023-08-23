""" diginitu """


def main():
    """ asda """
    while True:
        num = int(input())
        if num == 0:
            break
        while len(str(num)) > 1:
            num = singledigit(num)
        print(num)


def singledigit(num):
    '''aaaa'''
    newnum = 0
    for i in str(num):
        newnum += int(i)
    return newnum


main()
