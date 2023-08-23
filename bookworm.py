""" read in limited time """


def main():
    """ dasdas """
    for _ in range(int(input())):
        read(float(input()), int(input()))


def read(time, amount):
    """ how many book you can read in a limited time """
    book = []

    for _ in range(amount):
        book.append(float(input()))

    book.sort()
    while sum(book) > time:
        book.pop()
    print(len(book))


main()
