""" leelad """


def main(string):
    """pair leelad not pair programming """
    ans = ''
    written = ''
    for i in string:
        if i not in written:
            written += i

    for i in written:
        if string.count(i) % 2 == 1:
            ans += i

    if ans == '':
        print("fully paired")
    else:
        print(ans)


main(input())
