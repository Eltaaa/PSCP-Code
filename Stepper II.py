""" repeat """


def main():
    """ repeat """
    m_num = int(input())
    n_num = int(input())

    if m_num < n_num:
        for i in range(m_num, n_num+1):
            print(i)
    else:
        for i in range(m_num, n_num-1, -1):
            print(i)


main()
