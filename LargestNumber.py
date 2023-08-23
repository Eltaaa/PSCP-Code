'''asdfsd'''


def main():
    '''yung'''
    num1 = (input())
    num2 = (input())
    num3 = (input())
    # brute force
    opt1 = int(num1+num2+num3)
    opt2 = int(num1+num3+num2)
    opt3 = int(num2+num1+num3)
    opt4 = int(num2+num3+num1)
    opt5 = int(num3+num1+num2)
    opt6 = int(num3+num2+num1)
    # highest
    highest = opt1
    if opt1 < opt2:
        highest = opt2
    if opt3 > highest:
        highest = opt3
    if opt4 > highest:
        highest = opt4
    if opt5 > highest:
        highest = opt5
    if opt6 > highest:
        highest = opt6
    print(highest)


main()
