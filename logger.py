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
            f.write (f"{name}; {surname}; {phone}; {address} \n")



def print_data():
    print (' PRINTING OUT from the first file: \n')
    with open('data_ver1.csv', 'r', encoding='utf-8') as f:
        data_first = f. readlines()
        data_first_list= []
        j=0
        for i in range(len(data_first)):
            if  data_first[i] == '\n' or data_first[i]== len(data_first) - 1:
                data_first_list.append('' . join(data_first[j : i + 1]))
                j=i
            print(''.join(data_first_list))
    
            
    
    print (' PRINTING OUT from the second file: \n')
    with open('data_ver2.csv', 'r', encoding='utf-8') as f:
            data_second = f. readlines()
            print(data_second)



input_data()
print_data()