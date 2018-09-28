import os,sys

from random import shuffle

def clear_and_greet():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('''
*********************************************
************** A Game of Cups ***************
*********************************************
''')


def swap_the_cups():
    clear_and_greet()
    cups = ['X', 0, 0] # cups represented in a list. X represents the ball inside the cup
    shuffles = 0

    while True:
        try:
            shuffle_me = int(input('How many times should the cups be shuffled: ')) # ask user how many times should be shuffled
            break
        except ValueError:
            clear_and_greet()
            print('Oops!! Seems like you didn\'t enter a number. Try again\n')
            continue
        
    print() # print() for empty space and readability

    while shuffles < shuffle_me:
        shuffles += 1
        shuffle(cups) # shuffles the cups randomly
        print('Postion during {} shuffle: {}'.format(shuffles, cups)) # print and track the position of the ball while shuffling

    if cups[0] == 'X':
        print()
        print('Position of the ball after the last shuffle: {}'.format(cups)) # Show the ball position inside list
        print()
        print('The ball is under the FIRST cup')
    elif cups[1] == 'X':
        print()
        print('Position of the ball after the last shuffle: {}'.format(cups))
        print()
        print('The ball is under the SECOND cup')
    else:
        print()
        print('Position of the ball after the last shuffle: {}'.format(cups))
        print()
        print('The ball is under the THIRD cup')


while True: # play game until user enter 'n'
    swap_the_cups()
    print()

    play_again = input('Play again? (Y/n): ')
    
    if play_again.lower() != 'n':
        continue
    else:
        sys.exit()