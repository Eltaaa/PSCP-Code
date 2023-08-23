""" med """


def main(size):
    """ finding median """
    lst = []
    for _ in range(size):
        lst.append(int(input()))
    lst.sort()
    # 0 1 2 3 4
    # len = 5
    # med = 2
    if len(lst) % 2:
        print("%.1f" % lst[int((len(lst) - 1)/2)])
    else:
        # 0 1 2 4 5 6
        # len = 6
        # med = 3
        num1 = lst[int(len(lst)/2)]
        num2 = lst[int(len(lst)/2 - 1)]
        print((num1 + num2)/2)


main(int(input()))
