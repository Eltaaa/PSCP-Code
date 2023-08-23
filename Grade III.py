""" grade """


def main(subject):
    """ uhh """
    addup_avg = 0
    for _ in range(subject):
        score = float(input())
        if score >= 95:
            addup_avg += 4
        elif score >= 90:
            addup_avg += 3.5
        elif score >= 85:
            addup_avg += 3
        elif score >= 80:
            addup_avg += 2.5
        elif score >= 75:
            addup_avg += 2
        elif score >= 70:
            addup_avg += 1.5
        elif score >= 65:
            addup_avg += 1
        elif score >= 60:
            addup_avg += 0.5
    print('%.2f' % (addup_avg/subject))
    avg = int(addup_avg/subject*100)/100
    print("%.2f" % avg)


main(int(input()))
