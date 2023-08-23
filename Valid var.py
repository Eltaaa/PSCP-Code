'''ValidVar'''


def main():
    '''ValidVar'''

    num = int(input())

    for _ in range(num):
        name = input()
        if not name.strip().isidentifier():
            print("Invalid")

        elif name == 'if' or name == 'else' or name == 'elif' or name == 'while' or \
                name == 'for' or name == 'True' or name == 'False' or name == 'continue' or \
                name == 'break' or name == 'return' or name == 'is' or name == 'in' or \
                name == 'and' or name == 'or' or name == 'from' or name == 'as' or \
                name == 'pass' or name == 'not' or name == 'def' or name == 'None':
            print("Invalid")
        else:
            print('Valid')


main()
