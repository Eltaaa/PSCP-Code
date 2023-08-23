'''Run Length Encoding'''


def main():
    '''Run Length Encoding'''
    chr = input()
    paper = ''
    ans = 1
    for i in range(len(chr)-1):
        elif chr[i] == chr[i+1]:
            ans += 1
        elif chr[i] != chr[i+1]:
            paper += str(ans) + chr[i]
            ans = 1
    print(paper)


main()
