""" Maffs """
import math


def main():
    """ a """
    a_1 = math.sin(math.radians(90))
    a_2 = (math.sin(math.radians(60)))**2
    a_3 = math.cos(math.radians(245**2))
    a_4 = math.cos(math.radians(45 + 135))
    print((a_1 + a_2)/(a_3 + a_4))

    print((math.factorial(16)*math.factorial(4))/math.factorial(8))

    b_1 = ((25 - 12)**2 + (12 - 15)**2)**0.5
    print(40/b_1)

    print(math.log(1234**4, 10))

    e_1 = math.log(4234, 5)
    e_2 = math.log(8191, 2)
    e_3 = math.log(156154, 10)
    e_4 = math.log(777, 7)
    e_5 = math.log(888, 8)
    e_6 = math.log(999, 9)

    print((e_1 + e_2 + 71*e_3)/(e_4 - e_5 - e_6))


main()
