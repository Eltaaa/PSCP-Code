'''asdfsd'''


def main():
    '''yung'''
    opt = input().lower()
    high = float(input())
    low = float(input())
    #
    if low > high:
        low, high = high, low
    #
    mid = float(input())
    if mid > high:
        low, mid, high = low, high, mid
    elif mid < low:
        low, mid, high = mid, low, high
    #
    if opt == 'ascend':
        print('%.2f, %.2f, %.2f ' % (low, mid, high))
    else:
        print('%.2f, %.2f, %.2f ' % (high, mid, low))


main()
