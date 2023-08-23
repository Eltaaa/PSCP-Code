""" bts """


def main(day, age, height):
    """ free or not """
    paid = True
    if age < 14 and height < 90:
        paid = False
    elif day == 'Children Day' and age < 14 and height <= 140:
        paid = False
    elif day == 'Senior Day' and age >= 60:
        paid = False

    if paid:
        print("PAY")
    else:
        print("FREE")


main(input(), float(input()), float(input()))
