""" Key """


def main(num):
    """ key is smth smth """
    part1 = 0
    for i in str(num):
        part1 += int(i)

    part2 = int(str(num)[-3:]) * 10
    key = part1 + part2
    if key < 1000:
        key += 1000
    print(str(key)[-4:])


main(int(input()))
