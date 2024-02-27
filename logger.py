from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"choose format: \n\n"
                    f" 1 variant: \n"
                    f"{name}\n {surname} \n {phone} \n {address}\n\n"
                    f"{name}; {surname}; {phone}; {address} \n"
                    f" choose, pls"))
    while var != 1 and var != 2:
        print('incorrect')
        var = int(input('type in: '))

    if var == 1:
        with open('data_ver1.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")

    elif var == 2:
        with open('data_ver2.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {address} \n")


def print_data():
    print(' PRINTING OUT from the first file: \n')
    with open('data_ver1.csv', 'r', encoding='utf-8') as f:
        data_first = f. readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or data_first[i] == len(data_first) - 1:
                data_first_list.append('' . join(data_first[j: i + 1]))
                j = i
            print(''.join(data_first_list))

    print(' PRINTING OUT from the second file: \n')
    with open('data_ver2.csv', 'r', encoding='utf-8') as f:
        data_second = f. readlines()
        print(data_second)


def delete():
    print(' Please, choose file to proceed with: \n 1 or 2 ')
    var = int(input())
    while var != 1 and var != 2:
        print('incorrect')
        var = int(input('type in: '))
    if var == 1:
        with  open('data_ver1.csv', 'a', encoding='utf-8') as f:
    elif var == 2:
        with  open('data_ver2.csv', 'a', encoding='utf-8') as f:


def change():
    print(' Please, choose file to proceed with: \n 1 or 2 ')
    var = int(input())
    while var != 1 and var != 2:
        print('incorrect')
        var = int(input('type in: '))

    if var == 1:
        with open('data_ver1.csv', 'a', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        smthtochange = input("Type in what needs to be changed: ")
        newsmth = input("Type with what it should be replaced: ")
        # index= smthtochange.find(new)
        for i in range(len(data_first)):
            if data_first[i] == smthtochange:
                data_first[i] = data_first[i].replace(smthtochange, newsmth)
                print(data_first[i])

    elif var == 2:
        with open('data_ver2.csv', 'a', encoding='utf-8') as f:
            data_second = f. readlines()
            smthtochange = input("Type in what needs to be changed: ")
            newsmth = input("Type with what it should be replaced: ")
            # index= smthtochange.find(new)
            for i in range(len(data_first)):
                if data_first[i] == smthtochange:
                data_first[i] = data_first[i].replace(smthtochange, newsmth)
               



input_data()
print_data()
print("Please, what would you like to do next: 1- change 2 - delete 3 - exit")
v = int(input())
if v == 1:
    change()
elif v == 2:
    delete()
elif v == 3:
    break
else:
    print('incorrect')
    v = int(input('Try again : '))
