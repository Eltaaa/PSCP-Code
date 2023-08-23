""" ball """


def main(height):
    """ ricochet times """
    count = 0
    if height <= 0.01:
        print(0)
        return
    while height > 0.01:
        height = height*3/5
        count += 1
    print(count - 1)


main(float(input()))
