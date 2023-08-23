""" be ad """
 
 
def main(num):
    """ asdas """
    for _ in range(num):
        year = input()
        number = int(year[5:])
        if year[0:4] == 'B.E.':
            number -= 543
 
        if number % 100 == 0:
            number -= 1
 
        if number <= 0:
            print("ERROR")
        else:
            print('%d' % (number//100+1))
 
 
main(int(input()))