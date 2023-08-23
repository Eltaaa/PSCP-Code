""" worthiest depth"""


def main():
    '''dig down'''
    depth = int(input())
    int(input())
    mine = [[] for _ in range(depth)]
    for lst in mine:
        inp = input().split()
        lst.extend(map(int, inp))

    # print(*mine, sep="\n")
    depth_record = [sum(lst) for lst in zip(*mine)]
    # depth_record = []
    # for i in range(width):
    #     worth = 0
    #     for j in range(depth):
    #         worth += int(mine[i][j])
    #     depth_record.append(worth)
    print(max(depth_record))


main()
