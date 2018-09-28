import random
import os, sys

from random import shuffle

# The Rules
# 1) N stones forming a sequence labeled 1 to N. -> input N stones
# 2) Alice and Bob take 2 cosecutive stones until there no consectutive stones left.
#    the number of the stone left determines the winner
# 3) Alice plays first

def clear_and_greet():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('''
*********************************************
**************** Alice N Bob ****************
************* A Game of Stones **************
*********************************************
''')

def start_game():
    '''
    For now, the game only creates a list that contains the number of stones inputted by the user.
    And then it checks if the last 'stone' in the last is odd. If odd Alice wins the game.
    '''
    clear_and_greet() # clears screen and shows game "logo"

    print('Enter number of stones:\n') # ask user for the sequence of stones
    n = int(input('>  '))
    
    clear_and_greet() # clears screen and shows game "logo"
    
    stones = list(range(1, n+1)) # create (list) sequence of stones
    shuffle(stones) # shuffle the sequence of stones to have them in a random order
    print('The stones are: {}\n'.format(stones))

    if stones[-1] % 2 == 1: # Checks if the last stone in sequence is odd. If odd Alice wins.
        print('Last stone is {}. Alice wins!!!'.format(stones[-1]))
    else:
        print('The last stone is ({}). Bob wins!!!'.format(stones[-1]))

while True:
    start_game()

    play_again = input('\nWould you like to play again? (Y/n): ') # ask if player wants to play again

    if play_again.lower() != 'n':
        continue
    else:
        sys.exit()





    
