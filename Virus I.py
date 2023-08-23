""" Virus """


def main(virus):
    """ count birus body part """
    count = 0
    for i in virus:
        if i == "o":
            count += 1
    print(count)


main(input())
