""" prnigles """


def main():
    """ dsada """
    circumference = input()
    can = input()
    input()
    length = int(input())
    pringles = can.count(')')

    picked = 0
    for i in range(length):
        if can[i] == ')':
            picked += 1

    if picked == pringles:
        result = 'None.'
    else:
        result = 'There are still some left.'

    remaining = ' '*length + can[length:]

    print(picked)
    print(result)
    print(circumference)
    print(remaining)
    print(circumference)


main()
