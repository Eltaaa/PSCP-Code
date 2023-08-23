""" aaa """
# 38
# 45
# 42
# 25
# 16
# 27
# 87
# 50

def main():
    '''aa'''
    num = int(input()) 
    highest = num
    num = int(input())
    highest = is_higher(num, highest)
    num = int(input())
    highest = is_higher(num, highest)
    num = int(input())
    highest = is_higher(num, highest)
    num = int(input())
    highest = is_higher(num, highest)
    num = int(input())
    highest = is_higher(num, highest)
    num = int(input())
    highest = is_higher(num, highest)
    num = int(input())
    highest = is_higher(num, highest)

    print(highest)


def is_higher(num, highest):
    """is higher"""
    if num > highest:
        return num
    else:
        return highest


main()
