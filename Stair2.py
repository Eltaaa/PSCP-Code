""" asdas """


def main(height, num):
    """ dasdas """
    lst = []
    for _ in range(num):
        lst.append(int(input()))
    for i in lst:
        if i > height:
            print('No')
            return
    print(lst)
    lst = merge(lst, height)
    print(lst)

def merge(lst, height):
    '''merge into 1 single step if possible'''
    newlst = []
    for i in range(0, len(lst)-1):
        if lst[i] + lst[i-1] <= height:
            continue
        if lst[i] + lst[i+1] <= height:
            newlst.append(lst[i]+lst[i+1])
        else:
            newlst.append(lst[i])
    return newlst


main(int(input()), int(input()))
