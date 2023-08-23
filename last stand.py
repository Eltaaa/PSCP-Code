''' course '''


def main():
    '''Full Course: [] Reversed: []'''
    lst = input()[1:-1].split(",")
    for i in lst:
        print(i[-1])


main()
