""" Grader """


def main():
    """ fdsfds """
    start = int(input())
    end = int(input())
    addup = 0
    passnum = ""
    # Ascend
    if start <= end:
        if is_odd(start):
            start += 1
        for i in range(start, end+1, 2):
            passnum += " %d" % i
            addup += i
    # Descend
    if start > end:
        if is_odd(start):
            start -= 1
        for i in range(start, end-1, -2):
            passnum += " %d" % i
            addup += i
    print("pass :" + passnum)
    print("Sum :", addup)


def is_odd(num):
    '''is odd'''
    if num % 2:
        return True
    return False


main()
