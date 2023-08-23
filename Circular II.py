'''asdfsd'''


def main():
    '''yung'''
    xme = float(input())
    yme = float(input())
    radme = float(input())
    xfriend = float(input())
    yfriend = float(input())
    radfriend = float(input())
    distance = ((xme-xfriend)**2+(yme-yfriend)**2)**0.5

    if distance < radme + radfriend:
        print('Yes')
    else:
        print('No')


main()
