""" point sort """


def main(num):
    """ asdsa """
    for _ in range(num):
        lst = []
        for _ in range(int(input())):
            pair = [int(x) for x in input().split()]

            lst.append(pair)
        # lst.sort(key=lambda x: (x[0]))
        lst.sort(key=lambda x: (sum(x), x[0]))

        for i in lst:
            print(*i)


main(int(input()))
