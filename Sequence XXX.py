""" seq 30 """


def main(num, amount):
    """ dasasd """
    size = int((num - 1)/2)
    string = ""
    for rows in range(size, -size - 1, -1):
        for col in range(-size, size + 1):
            con1 = rows == size or rows == -size
            con2 = col == -size or col == size
            con3 = rows + col == 0
            con4 = rows == col
            if con1 or con2 or con3 or con4:
                string += "*"
            else:
                string += " "
        for _ in range(amount):
            print(string, end=" ")
        string = ""
        print()


main(int(input()), int(input()))
