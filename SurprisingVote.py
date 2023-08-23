""" surprisingvote """


def main():
    """ fsd """
    score = float(input())
    highest = float(input())
    remain = 0
    if highest*2 < score:
        # set mid score to highest possible, hence remain == third vote
        # score28, vote = 10 10 8
        remain = score - highest*2
    if highest - remain > 2:
        print('Surprising')
    else:
        print('Not surprising')


main()
