'''docstring'''


def main():
    '''asdas'''
    string = input().split(" ")
    tup = tuple(string)
    char = input()
    numchar = tup.count(char)
    indchar = tup.index(char)


'''docstring'''


def main():
    '''asdas'''
    cat = []

    while True:
        breed = input()
        bred = breed.split(", ")
        if breed == "IT'S A DOG":
            cat.pop()
            continue
        elif breed == "END":
            break
        cat.extend(bred)
    cat2 = cat.copy()
    cat2.sort()
    cat3 = []
    for i in cat2:
        if i not in cat3:
            cat3.append(i)
    for i in cat3:
        print(i, cat.index(i)+1, cat.count(i))


main()
  for _ in range(numchar):
       for _ in range(numchar):
            print(indchar, end=" ")
        print()


main()
