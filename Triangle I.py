'''asdfsd'''


def main():
    '''yung'''
    # opt = input().lower()
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
    if abs(low**2 + mid**2 - high**2) <= 0.01:
        print('Yes')
    else:
        print('No')


main()
