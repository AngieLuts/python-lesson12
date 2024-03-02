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
    print(' Please, tell me what file should I print out: \n 1 - first \n 2 - second \n 3 - both \n')
    file = int (input())

    while file < 1 and file >3:
        print('incorrect')
        file = int(input('type in 1, 2 or 3: '))
    if file == 1:
        print("Printing out from the first file")
        with open('data_ver1.csv', 'r', encoding='utf-8') as f:
            data_first = f. readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or data_first[i] == len(data_first) - 1:
                    data_first_list.append('' . join(data_first[j: i + 1]))
                    j = i
                print(''.join(data_first_list))
                return data_first
    elif file == 2:
        print(' PRINTING OUT from the second file: \n')
        with open('data_ver2.csv', 'r', encoding='utf-8') as f:
            data_second = f. readlines()
            print(*data_second)
        return data_second
    else:
        print("Printing out from the first file")
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
            print(*data_second)
        return data_first, data_second


def change_line(dataFile, num_of_the_row, file_num):
    answer = input(f"Change this info ? \n{dataFile[num_of_the_row]}?\n Type in your answer: ")
    while answer != 'yes':
        num_of_the_row = int(input('Please, type in number of the row we need to change: ')) - 1
    print(f"We change this info: \n{dataFile[num_of_the_row]}\n")
    if file_num == 1:
        name = dataFile[num_of_the_row].split('\n')[0]
        surname = dataFile[num_of_the_row].split('\n')[1]
        phone = dataFile[num_of_the_row].split('\n')[2]
        address = dataFile[num_of_the_row].split('\n')[3]
    if file_num== 2:
        name = dataFile[num_of_the_row].split(';')[0]
        surname = dataFile[num_of_the_row].split(';')[1]
        phone = dataFile[num_of_the_row].split(';')[2]
        address = dataFile[num_of_the_row].split(';')[3]

    answer = int(input(f"What would you like to change?\n"
                       f"1. Name\n"
                       f"2. Surname\n"
                       f"3. Phone number\n"
                       f"4. Address\n"
                       f"Please, type in your answer: "))
    while answer < 1 or answer > 4:
        print("Probably, you've mistyped \n Please, type in number in range between 1 and 4")
        answer = int(input(f"What would you like to change?\n"
                       f"1. Name\n"
                       f"2. Surname\n"
                       f"3. Phone number\n"
                       f"4. Address\n"
                       f"Please, type in your answer: "))
    if answer == 1:
        name = name_data()
    elif answer == 2:
        surname = surname_data()
    elif answer == 3:
        phone = phone_data()
    elif answer == 4:
        address = address_data()

    if file_num == 1:
        data_first = dataFile[:num_of_the_row] + [f'{name}\n{surname}\n{phone}\n{address}'] + \
        dataFile[num_of_the_row+ 1:]
        if num_of_the_row+ 1 == len(dataFile):
            data_first = dataFile[:num_of_the_row] + [f'{name}\n{surname}\n{phone}\n{address}\n']
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Your changes have been succesfully saved')
    else:
        data_second = dataFile[:num_of_the_row] + [f'{name};{surname};{phone};{address}'] + \
                    dataFile[num_of_the_row+ 1:]
        if num_of_the_row + 1 == len(dataFile):
            data_second = dataFile[:num_of_the_row] + [f'{name};{surname};{phone};{address}\n']
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Your changes have been succesfully saved')

def change():
    print('Please, choose number of the file, you need make changes in.')
    data_first, data_second = print_data()
    number_file = int(input('Please, type in the number: '))

    while number_file != 1 and number_file != 2:
        print("Probably, you've mistyped")
        number_file = int(input('Please, type in the number: '))

    if number_file == 1: 
        print("Have you decided which line should be changed? Please, think")
        number_journal = int(input('Please, type in the number of the row: '))
        number_journal -= 1
        change_line(data_first, number_journal, 1)
    else:
        print("Have you decided which line should be changed? Please, think")
        number_journal = int(input('Please, type in the number of the row: '))
        number_journal -= 1
        change_line(data_second, number_journal, 2)


def delete():
    print('Please, choose number of the file, where you need to delete some info.')
    data_first, data_second = print_data()
    number_file = int(input('Please, type in the number: '))

    while number_file != 1 and number_file != 2:
        print("Probably, you've mistyped")
        number_file = int(input('Please, type in the number: '))
    if number_file == 1: 
        print("Have you decided which line should be deleted? Please, think")
        number_journal = int(input('Please, type in the number of the row:  '))
        print(f'Please, answer yes or no. \n Are you sure we need to delete : \n{data_first[number_journal - 1]}?')
        answer=input()
        while answer != 'yes' and answer != 'no':
            print("Probably, you've mistyped. Just yes or no")
            answe = input()
        if answer == 'yes':
            data_first = data_first[:number_journal - 1] + data_first[number_journal + 1:]
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(''.join(data_first))
                print('Your changes have been succesfully saved')
        elif answer == 'no':
            delete()
    else:
        print("Have you decided which line should be deleted? Please, think")
        number_journal = int(input('Please, type in the number of the row:  '))
        print(f'Please, answer yes or no. \n Are you sure we need to delete : \n{data_second[number_journal - 1]}')
        answer=input()
        if answer == 'yes':
            data_second = data_second[:number_journal] + data_second[number_journal + 1:]
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(''.join(data_second))
                print('Your changes have been succesfully saved')
        else:
            delete()




##------------------------------------------------------------------------------------------
##Здесь ниже я  оставила один из вариантов того, как я самостоятельно пыталась реализовать функции изменения и удаления через поиск нужной фразы. 
# Но у меня не получилось. Может сможете подсказать реально ли с этой стороны реализовать решение задания?

""" def delete():
    smthtodel = input("Type in what needs to be deleted: ")
    print(' Please, choose file to proceed with: \n 1 or 2 ')
    var = int(input())
    while var != 1 and var != 2:
        print('incorrect')
        var = int(input('type in: '))
    if var == 1:
        with open('data_ver1.csv', 'a', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first = data_first.remove(smthtodel)
    elif var == 2:
        with open('data_ver2.csv', 'a', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first = data_first.remove(smthtodel) """

""" def change():
    smthtochange = input("Type in what needs to be changed: ")
    newsmth = input("Type with what it should be replaced: ")
    print(' Please, choose file to proceed with: \n 1 or 2 ')
    var = int(input())
    while var != 1 and var != 2:
        print('incorrect')
        var = int(input('type in: '))

    if var == 1:
        with open('data_ver1.csv', 'a', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first = data_first.replace(smthtochange, newsmth)

    elif var == 2:
        with open('data_ver2.csv', 'a', encoding='utf-8') as f:
            data_second = f. readlines()
            data_second = data_second.replace(smthtochange, newsmth) """
