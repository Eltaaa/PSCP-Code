""" meteorite """


def main(initial, multi, safe):
    """ calculate missile needed to stop cataclysm """
    weight = initial
    cnt = 1
    shot = 0
    while weight >= safe:
        shot += cnt # shoot
        weight = weight / multi # weight reduce
        cnt *= multi # meteor multiply
    print(shot)
main(float(input()), int(input()), float(input()))
