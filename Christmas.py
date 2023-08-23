""" christmas """


def main(leaf_width, bark):
    """ print leaf and bark """
    leaf = "*"
    for _ in range(leaf_width):
        print(leaf.center(leaf_width*2 - 1))
        leaf += "**"

    for _ in range(bark):
        print("---".center(leaf_width*2 - 1))


main(int(input()), int(input()))
