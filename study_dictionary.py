def main():
    print("Hello World!")
    print("Starting study dictionary python script")
    # # tests simple number inputs
    # x1 = int(input('input x1: '))
    # x2 = int(input('input x2: '))
    # print('x1 + x2 = ' + str(x1 + x2))

    # # tests simple string inputs
    # first_name = input('first name: ')
    # last_name = input('last name: ')
    # print('my full name is ' + first_name + ' ' + last_name)

    # test dictionary
    this_dict = {
        'x1': 1,
        'x2': 2,
        'first name': 'Kibum',
        'last name': 'Kwon'
    }
    print('\nlist default items below')
    print('============================')
    for key in this_dict:
        print('key: ', end='')      # print without newline
        print(key, end='')          # print without newline
        print('\tvalue: ', end='')  # print without newline
        print(this_dict[key])
    print('============================\n')

    cmd = 0
    while cmd != 6:
        print('Choose what to to do with the dictionary')
        print('1. Add new item')
        print('2. Remove item using key')
        print('3. Edit item using key')
        print('4. Display item using key')
        print('5. List all items')
        print('6. Exit program')
        cmd_str = input('Type command number: ')
        if cmd_str.isdigit():
            cmd = int(cmd_str)
        else:
            cmd = 0

        match cmd:
            case 1:
                key = input('Type key to add a new item: ')
                if key in this_dict:
                    print('item with the key already exists. Try again with different key')
                else:
                    value = input('Type value for new item: ')
                    this_dict[key] = value
                    print('new item [' + key + ', ' + value + '] is added\n')
            case 2:
                key = input('Type key to remove a item: ')
                if key in this_dict:
                    del this_dict[key]
                    print('A item with the key \'' + key + '\' was removed')
                else:
                    print('item does not exist with the key.')
                print('\n')
            case 3:
                key = input('Type key to remove a item: ')
                if key in this_dict:
                    old_value = this_dict[key]
                    value = input('Type value for new item: ')
                    this_dict[key] = value
                    print(old_value + ' is replaced to ' + value + ' in this_dict[' + key + ']')
                else:
                    print('item does not exist with the key.')
            case 4:
                key = input('Type key to find value: ')
                if key in this_dict:
                    print('value searched with key \'' + key + '\': ', end='')
                    print(this_dict[key])
                    print('\n')
                else:
                    print('key cannot be found in dictionary. Try again with different key.\n')
            case 5:
                print('\nlist items below')
                for key in this_dict:
                    print('key: ', end='')  # print without newline
                    print(key, end='')  # print without newline
                    print('\t\t\t\tvalue: ', end='')  # print without newline
                    print(this_dict[key])
                print('\n')
            case 6:
                print('Selected exiting program.')
            case default:
                cmd = 0
                print(cmd)


if __name__ == "__main__":
    main()
    print('\n\nExiting program... Bye~')
