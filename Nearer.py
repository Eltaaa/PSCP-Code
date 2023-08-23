""" Nearer """


def main(alice, bob, ice):
    """ nearer """
    bob_dist = abs(bob - ice)
    alice_dist = abs(alice - ice)

    if alice_dist < bob_dist:
        print('Alice %d' % alice_dist)
    elif alice_dist > bob_dist:
        print('Bob %d' % bob_dist)
    else:
        print('Sundaes %d' % bob_dist)


main(int(input()), int(input()), int(input()), )
