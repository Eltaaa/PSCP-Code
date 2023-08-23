""" iphong """


def main(name, storage):
    """ fdskl """
    availity = False
    price = 0
    if name == 'iPhone 13 mini':
        availity = True
        price = 25900
    elif name == 'iPhone 13':
        availity = True
        price = 29900
    elif name == 'iPhone 13 Pro':
        availity = True
        price = 38900
    elif name == 'iPhone 13 Pro Max':
        availity = True
        price = 42900

    if name == 'iPhone 13 mini':
        price += i13mini(storage)
    elif name == 'iPhone 13':
        price += i13(storage)
    else:
        price += i13pro(storage)

    i13storage = ['128 GB', '256 GB', '512 GB']
    i13prostorage = ['128 GB', '256 GB', '512 GB', '1 TB']
    if (name == 'iPhone 13 mini' or name == 'iPhone 13') and \
            storage not in i13storage:
        availity = False
    elif (name == 'iPhone 13 Pro' or name == 'iPhone 13 Pro Max') and \
            storage not in i13prostorage:
        availity = False

    if availity == True:
        print(int(price))
    else:
        print("Not Available")


def i13mini(storage):
    ''' additional price for i13 (mini) '''
    additional = 0
    if storage == "256 GB":
        additional = 3000
    elif storage == "512 GB":
        additional = 12000
    return additional


def i13(storage):
    ''' additional price for i13 (mini) '''
    additional = 0
    if storage == "256 GB":
        additional = 4000
    elif storage == "512 GB":
        additional = 13000
    return additional


def i13pro(storage):
    """ additonal price for i13 pro (max) """
    additional = 0
    if storage == "256 GB":
        additional = 4000
    elif storage == "512 GB":
        additional = 12000
    elif storage == "1 TB":
        additional = 20000
    return additional


main(input(), input())
