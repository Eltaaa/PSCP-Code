""" dasdas """


def main(num):
    """ jklldasdsasd """
    wage = 0
    for _ in range(num):
        hours = float(input())
        if hours % 1 != 0:
            hours = int(hours + 1)
        wage += hours * 8720
    print('%d' % wage)
main(int(input()))
