""" 6174 """


def main(num):
    """ klfjsdklf """
    # high = highnum(num)
    # low = highnum(num)[-1::-1]
    # print(high, low)
    num = "%04d" % int(num)
    count = 0
    while num != "6174":
        high = highnum(num)
        low = high[-1::-1]
        newnum = int(high) - int(low)
        count += 1
        num = "%04d" % (newnum)
    print(count)


def highnum(num):
    '''make highest number possible'''
    lst = [int(i) for i in num]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    string = ""
    for i in lst:
        string += str(i)
    return string


main(input())
