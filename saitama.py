""" saitama """


def main(push, sit, look, run):
    """ dsads """
    pperday = int(input())
    sperday = int(input())
    rperday = int(input())
    lperday = int(input())

    push_day = push / pperday
    ans = round_day_up(push_day)

    sit_day = round_day_up(sit / sperday)
    ans = highest(ans, sit_day)

    look_day = round_day_up(look / lperday)
    ans = highest(ans, look_day)

    run_day = round_day_up(run / rperday)
    ans = highest(ans, run_day)

    print('%d' % ans)


def highest(ans, num):
    """ find highest number """
    if ans >= num:
        return ans
    return num


def round_day_up(num):
    """ round day up to int number """
    if num % 1 != 0:
        return int(num) + 1
    return int(num)


main(int(input()), int(input()), int(input()), int(input()))
