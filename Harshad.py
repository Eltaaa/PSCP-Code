""" sanity - 1 """


def main():
    """ dsadsa """
    for _ in range(10):
        num = int(input())
        if num == 0:
            print("No")
        else:
            if num % sumdigit(num) == 0:
                print("Yes")
            else:
                print('No')


def sumdigit(num):
    '''sum of its digits'''
    divider = 0
    num = abs(num)
    for i in str(num):
        divider += int(i)
    return divider


main()
