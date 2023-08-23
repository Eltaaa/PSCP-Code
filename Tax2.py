""" tax evasiom """


def main(income):
    """ ssss """
    if 0 <= income <= 150000:
        tax = phase1(income)
    elif income <= 300000:
        tax = phase2(income)
    elif income <= 500000:
        tax = phase3(income)
    elif income <= 750000:
        tax = phase4(income)
    elif income <= 1000000:
        tax = phase5(income)
    elif income <= 2000000:
        tax = phase6(income)
    elif income <= 4000000:
        tax = phase7(income)
    else:
        tax = phase8(income)
    print('%d = %d' % (income, tax))


def phase1(num):
    ''' no tax'''
    return 0*num


def phase2(num):
    ''' 5% '''
    if 150000 < num <= 300000:
        tax = 0.05*(num-150000)
    else:
        tax = 0.05*(300000-150000)
    return tax + phase1(num)


def phase3(num):
    ''' 10% '''
    if 300000 < num <= 500000:
        tax = 0.1*(num-300000)
    else:
        tax = 0.1*(500000 - 300000)
    return tax + phase2(num)


def phase4(num):
    ''' 15% '''
    if 500000 < num <= 750000:
        tax = 0.15*(num-500000)
    else:
        tax = 0.15*(750000 - 500000)
    return tax + phase3(num)


def phase5(num):
    ''' 20%'''
    if 750000 < num <= 1000000:
        tax = 0.2*(num - 750000)
    else:
        tax = 0.2*(1000000 - 750000)
    return tax + phase4(num)


def phase6(num):
    ''' 25%'''
    if 1000000 < num <= 2000000:
        tax = 0.25*(num - 1000000)
    else:
        tax = 0.25*(1000000)
    return tax + phase5(num)


def phase7(num):
    ''' 30%'''
    if 2000000 < num < 4000000:
        tax = 0.3*(num - 2000000)
    else:
        tax = 0.3*(2000000)
    return tax + phase6(num)


def phase8(num):
    """ 35% """
    tax = 0.35*(num - 4000000)
    return tax + phase7(num)


lst = [0, 100000, 150000, 200000, 300000, 400000, 500000, 600000, 750000, 800000, 1000000, 1100000, 2000000, 3000000, 4000000, 5000000]

for i in lst:
    main(i+1)

