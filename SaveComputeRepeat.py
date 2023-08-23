'''afds'''


def main():
    '''aa'''
    start = 492137954293754252786

    millisec = start
    sec = millisec//1000
    millisec = millisec % 1000
    minute = sec//60
    seconds = sec % 60
    hours = minute//60
    minutes = minute % 60
    days = hours//24
    hours = hours % 24

    print(days, hours, minutes, seconds, millisec)


main()
