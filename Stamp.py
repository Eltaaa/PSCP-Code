"""Stamp"""


def main():
    """Stamp"""
    count = int(input())
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    total = 0
    stamp = 0
    for _ in range(count):
        bill = int(input())
        while bill > 0 and stamp >= numc:
            stamp -= numc
            bill = max(bill - numd, 0)
        total += bill
        stamp += numb * (bill // numa)
    print(str(total) + '\n' + str(stamp))


main()
