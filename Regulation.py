'''afds'''


def main():
    '''aa'''
    xxx = (int(input()))
    yyy = float(input())
    zzz = input()
    print(" "*(30-len(str(xxx))) + str(xxx))
    print("%030d" % xxx)
    print("%.2f" % yyy)
    print("%.12f" % yyy)
    print(" "*(40-len(zzz)) + str(zzz))


main()
