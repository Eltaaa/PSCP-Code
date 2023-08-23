'''afds'''


def main():
    '''aa'''
    start = int(input())
    s_var = int(input())
    m_var = int(input())
    h_var = int(input())
    sec = start
    minute = sec//s_var
    seconds = sec % s_var
    hours = minute//m_var
    minutes = minute % m_var
    days = hours//h_var
    hours = hours % h_var

    # print(days, hours, minutes, seconds)
    print('0'*days+"%d:%d:%d" % (hours, minutes, seconds))


main()
