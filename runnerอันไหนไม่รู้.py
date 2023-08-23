""" runner """


def main(distance, runners):
    """ dadas """
    match = [input().split() for _ in range(runners)]
    lst = match.copy()
    lst.sort(key=lambda x: ((distance - int(x[1])) / int(x[0]), x[1]))
    # # print(match)
    # time = []
    # for i in match:
    #     time.append((distance - int(i[1])) / int(i[0]))
    # fastest = time.index(min(time))
    # print(fastest +1)
    # print(match)
    # print(lst)
    print(match.index(lst[0]) + 1)

main(float(input()), int(input()))
