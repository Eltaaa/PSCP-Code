""" apirty """


def main(num, choice):
    """ dsadsa """
    cnt = 0
    for i in num:
        if i == "1":
            cnt += 1

    if cnt % 2 == 1 and choice == "Even":  # odd cnt and even
        print(num + "1")
    elif cnt % 2 == 1 and choice == "Odd":
        print(num + "0")
    elif cnt % 2 == 0 and choice == "Even":
        print(num + "0")
    else:
        print(num + "1")


main(input(), input())
