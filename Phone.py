""" dasdas """


def main(number, inter):
    """ asd """
    num_type = ''
    if len(str(number)) == 9:
        num_type = 'home'
    else:
        num_type = 'mobile'

    if num_type == 'home' and inter == 'Domestic':
        print('0', number[1:5], number[5:])
    elif num_type == 'home' and inter == 'International':
        print('+66', number[1:5], number[5:])
    elif num_type == 'mobile' and inter == 'Domestic':
        print(number[0:2], number[2:6], number[6:])
    elif num_type == 'mobile' and inter == 'International':
        print('+66' + number[1:2], number[2:6], number[6:])


main(input(), input())
