import caryard

"""  
   Task 1:  Implement menu function      

   Menu function prompts the user for a input. Invalid message is shown  until the valid
   menu option (1-5) is entered. 

  *See the screen shot provided: menu

"""


def menu():
    print()
    print('\tCar Yard')
    print('1. Buy')
    print('2. Sell')
    print('3. Search')
    print('4. Show all')
    print('5. Quit\n')
    available_commands = ['1', '2', '3', '4', '5']
    while True:
        command = input("Your option[1-5] :")

        if command in available_commands:
            return int(command)

        print('Invalid option! Must be between 1 and 5')


def main():
    caryard.load_cars()

    while True:

        option = menu()

        if option == 1:
            caryard.buy_car()
        elif option == 2:
            caryard.sell_car()
        elif option == 3:
            caryard.search_car()
        elif option == 4:
            caryard.list_all_cars()
        elif option == 5:
            caryard.quit_car()
            break
        else:
            print("Invalid menu option!")


# Calling main for the execution of the Car yard application
if __name__ == '__main__':
    main()



