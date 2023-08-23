""" aaa """
 
 
def main():
    '''aa'''
    start = int(input())
 
    sec = start
    minute = sec//60
    seconds = sec % 60
    hours = minute//60
    minutes = minute % 60
    days = hours//24
    hours = hours % 24
 
    if days > 9999:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d" % (days, hours, minutes, seconds))
 
 
main()