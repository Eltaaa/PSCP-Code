""" rock paper scissors """


def main(battle):
    """ fdssdf """
    win, lose = 0, 0

    while len(battle) > 0:
        vic, defeat = result(battle[:2])
        battle = battle[2:]
        win += vic
        lose += defeat

    if win == lose:
        print("DRAW", win)
    elif win > lose:
        print("A win %d-%d" % (win, lose))
    else:
        print("B win %d-%d" % (lose, win))


def result(string):
    """ get result """
    vic = 0
    lose = 0
    # by the way "tire" variable is unused but good to have in this code
    if string[0] == string[1]:
        vic = 0
    elif string[0] == "R" and string[1] == "S":
        vic = 1
    elif string[0] == "P" and string[1] == "R":
        vic = 1
    elif string[0] == "S" and string[1] == "P":
        vic = 1
    else:
        lose = 1

    return vic, lose


main(input())
