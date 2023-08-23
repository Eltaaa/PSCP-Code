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
