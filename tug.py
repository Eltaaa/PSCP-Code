""" tug """


def main():
    """ get a b team """
    atotal = get()
    btotal = get()

    if atotal < btotal:
        print('A')
    elif btotal < atotal:
        print('B')
    else:
        print('AB')
def get():
    """ get total F """
    force = 0
    for _ in range(10):
        force += int(input())
    return force
main()
