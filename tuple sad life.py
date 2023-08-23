'''docstring'''


def main():
    '''asdas'''
    string = input().split(" ")
    tup = tuple(string)
    char = input()
    numchar = tup.count(char)
    indchar = tup.index(char)

    for _ in range(numchar):
        for _ in range(numchar):
            print(indchar, end=" ")
        print()


main()
