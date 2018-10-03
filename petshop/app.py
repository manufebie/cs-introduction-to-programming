import os, sys
from petshop import Animal, Petshop

petshop1 = Petshop('The furry shop')
start = '''
********************************
         THE PET SHOP
********************************
'''

# instanciate animals


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(start)

menu1 = ['[1] Buy pet', '[2] Sell Pet', '[3] See pets', '[4] Quit program']

def menu():
    clear()
    for option in menu1:
        print(option)

def main():
    menu()

    print()
    choice = int(input('> '))

    if choice == 1:
        clear()
        name = input('Type animal you want to buy: ') # type animal you want to buy
        petshop1.add_pet(name) # animal gets appended to list
        petshop1.diplay_pets() # go back to menu1
    elif choice == 2:
        clear()
        print('Choose Animal you want to sell (Choose by number)')
        petshop1.diplay_pets()
        print()
        index_animal = int(input('> '))
        print()
        petshop1.del_pet(index_animal)
        menu()
    elif choice == 3:
        clear()
        print('Animals available in your shop. Type "Q" to go back\n')
        
        petshop1.diplay_pets()
        
        print()
        
        choice = input('> ')
        if choice.lower() == 'q':
            menu()
    else:
        sys.exit()

while True:
    main()