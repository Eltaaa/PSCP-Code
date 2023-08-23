''' course '''


def main():
    '''Full Course: [] Reversed: []'''
    lst = input()[1:-1].split(", ")
    ans = []
    for i in lst:
        if int(i) % 2 == 0 and int(i) != 0:
            ans.append(i)
    if len(ans) == 0:
        print("Nope")
    else:
        for i in ans:
            print(i)


main()
