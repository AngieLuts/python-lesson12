from logger.py import input_data(), print_data()


def interface():
   print("Добрый день! Вы попали на страницу бота-справочника. \n 1-input \n 2 -choose")
   command = int(input('type in number: '))
   
   while command != 1 and command != 2:
        print("incorrect")
        command = int(input('type in number: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()


    
