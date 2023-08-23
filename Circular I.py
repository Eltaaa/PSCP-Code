'''asdfsd'''


def main():
    '''yung'''
    xme = float(input())
    yme = float(input())
    rad = float(input())
    xyung = float(input())
    yyung = float(input())
    distance = ((xme-xyung)**2+(yme-yyung)**2)**0.5

    if distance <= rad:
        print('Yes')
    else:
        print('No')


main()
