""" aaa """


def main():
    '''aa'''
    print(dozen1() + dozen2())


def dozen1():
    '''a'''
    wing_count = 0
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    return wing_count


def dozen2():
    '''a'''
    wing_count = 0
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    weight = float(input())
    wing_count += weight_check(weight)
    return wing_count


def weight_check(num):
    '''50-70'''
    if abs(num-60) <= 10:
        return 1
    else:
        return 0


main()
