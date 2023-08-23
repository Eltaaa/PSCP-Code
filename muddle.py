""" muddle """


def main():
    """ dasdsa """
    lst = []
    while True:
        course = input()
        if course == "DONE":
            break

        elif course == "SOMETHING'S WRONG":
            lst.clear()
            continue

        elif "Can't do: " in course:
            lst.remove(course[course.index(":") + 2:])
            continue

        elif course == "CLOSED":
            lst.clear()
            break

        menu = course[:course.index("#")-1]
        order = course[course.index("#") + 1:]
        if order == "N":
            lst.append(menu)
            continue
        lst.insert(int(order) - 1, menu)

        # print("===")
        # print(lst)
        # print("===")

    print("Full Course:", lst, end=" ")
    lst.reverse()
    print("Reversed:", lst)


main()
