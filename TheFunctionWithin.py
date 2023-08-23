""" aaa """


def main(num1, num2, num3, num4):
    """ bbb """
    # line 1
    print(ffunc(ffunc(num1)))

    # line 2
    print(gfunc(ffunc(num1 - num2)))

    # line 3
    print(hfunc(ffunc(num1 + num2), ffunc(num1 + num3), gfunc(ffunc(num4**2))))

    # line 4
    para1 = hfunc(ffunc(num1 + num2), ffunc(num1 - num3),
                  gfunc(ffunc(num4**2)))
    para2 = gfunc(ffunc(num1 - num2))
    para3 = ffunc(ffunc(ffunc(ffunc(ffunc(num3)))))
    para4 = num4**8

    print(ifunc(para1, para2, para3, para4))


def ffunc(num):
    '''f(x)'''
    return num*2


def gfunc(num):
    '''g(x)'''
    return 3*num**4 - num**3 + 2*num**2 + 10


def hfunc(num, num1, num2):
    '''h(x, y, z)'''
    return (num2 + num)**2 - num*num1 + num1**2


def ifunc(num1, num2, num3, num4):
    '''i(a, b, c, d)'''
    return (num1**2 + num2**2 - num3**2)/(num4**2 - 2*num1*num4 + 2*num1)


main(float(input()), float(input()), float(input()), float(input()))
