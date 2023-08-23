''' course '''


def main():
    '''Full Course: [] Reversed: []'''
    course = []
    while True:
        inp = input()
        if inp != "NULL":
            course.append(inp)
        else:
            break

    course.reverse()
    for i in course:
        print(i)


main()
''' course '''


def main():
    '''Full Course: [] Reversed: []'''
    num = []
    xxx = int(input())

    while True:
        inp = int(input())
        if inp == 0:
            break
        else:
            num.append(inp)
            # xxx.append(inp)
    num.sort()
    for i in range(1, xxx + 1):
        if i not in num:
            print(i)


main()
