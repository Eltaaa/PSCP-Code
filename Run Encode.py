""" fdsf """


def main(run):
    """ running """
    count = 1
    if len(run) == 1:
        print("1%s" % run)
    while len(run) > 1:
        if run[0] == run[1]:
            count += 1
        else:
            print(str(count) + run[0], end="")
            count = 1
        run = run[1:]
        if len(run) == 1:
            print(str(count) + run[0])


main(input())
