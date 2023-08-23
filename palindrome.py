""" adasdas """


def main(num, time):
    """ palindrome 24 clock """

    hours = time[-5:-3]
    natee = time[-2:]
    natee = "%02d" % (int(natee) + 1)
    get = 0
    while get < num:
        if natee == "60":
            natee = "00"
            hours = str(int(hours) + 1)

        if hours == "24":
            hours = "0"

        if ispalindrome(hours, natee):
            print("%d:%02d" % (int(hours), int(natee)))
            get += 1
        natee = "%02d" % (int(natee) + 1)


def ispalindrome(txt1, txt2):
    ''' return true if palindrome'''

    if txt1 + txt2 == txt2[::-1] + txt1[-1::-1]:
        return True
    return False


main(int(input()), input())
