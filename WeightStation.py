""" weight station """


def main(avg, point1, point2, point3):
    """ find missing spot weight """
    overall_weight = avg*4
    if overall_weight > 15*1000:
        print("Overweight")
        return
    point4 = overall_weight - point1 - point2 - point3
    # Unbalanced condition
    con1 = abs(point1 - avg) > avg/2
    con2 = abs(point2 - avg) > avg/2
    con3 = abs(point3 - avg) > avg/2
    con4 = abs(point4 - avg) > avg/2

    if con1 or con2 or con3 or con4:
        print("Unbalance")
        return

    print("Pass %.2f" % point4)


main(float(input()), float(input()), float(input()), float(input()))
