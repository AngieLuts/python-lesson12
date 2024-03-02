from logger import input_data, print_data, change, delete


def interface():
    print(" Hey! This is my useful contacts database!")
    print("Please, what would you like to do next: \n 1- input new contact info \n 2 - change \n 3 - delete \n 4 -show contacts\n 5- exit \n")
    v = int(input())
    while v<1 or v>5:
        print('There must be a mistype. Please, try again. Here is a reminder for you:\n 1- input new contact info \n 2 - change \n 3 - delete \n 4 -show contacts\n 5- exit \n')

    if v == 1:
        input_data()
    elif v == 2:
        change()
    elif v == 3:
        delete()
    elif v == 4:
        print_data()
    else:
        print( " See you next time!")

        

#interface()


    
