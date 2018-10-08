import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('''
*********************************************
**************** Modulo 42 ****************
*********************************************
''')


def main():
    clear()

    print('Enter 10 numbers: \n') # ask user to input an integer 10 x

    for i in range(10):
        i += 1 # loop 10 x to ask for user input

        try: # try/except block to check if user inputs an integer
            x = int(input('(Input number) > '))
            x = x % 3
        except ValueError:
            print('Only positive numbers allowed')
            i -= 1 # goes one step back and continues
            continue
        
        print('(R) is: {}'.format(x)) # print remainder
        

main()


