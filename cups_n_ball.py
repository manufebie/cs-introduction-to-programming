'''
Jealous​ ​ of​ ​ Mirko’s​ ​ position​ ​ as​ ​ head​ ​ of​ ​ the​ ​ village,​ ​ Borko​ ​ stormed​ ​ into​ ​ his
tent​ ​ and​ ​ tried​ ​ to​ ​ demonstrate​ ​ Mirko’s​ ​ incompetence​ ​ for​ ​ leadership​ ​ with​ ​ a
trick.

Borko​ ​ puts​ ​ three​ ​ opaque​ ​ cups​ ​ onto​ ​ the​ ​ table​ ​ next​ ​ to​ ​ each​ ​ other​ ​ (opening
facing​ ​ down)​ ​ and​ ​ a ​ ​ small​ ​ ball​ ​ under​ ​ the​ ​ leftmost​ ​ cup.​ ​ He​ ​ then​ ​ swaps​ ​ two
cups​ ​ in​ ​ one​ ​ of​ ​ three​ ​ possible​ ​ ways​ ​ a ​ ​ number​ ​ of​ ​ times.​ ​ Mirko​ ​ has​ ​ to​ ​ tell
which​ ​ cup​ ​ the​ ​ ball​ ​ ends​ ​ up​ ​ under.

Wise​ ​ Mirko​ ​ grins​ ​ with​ ​ his​ ​ arms​ ​ crossed​ ​ while​ ​ Borko​ ​ struggles​ ​ to​ ​ move
the​ ​ cups​ ​ faster​ ​ and​ ​ faster.​ ​ What​ ​ Borko​ ​ does​ ​ not​ ​ know​ ​ is​ ​ that
programmers​ ​ in​ ​ the​ ​ back​ ​ are​ ​ recording​ ​ all​ ​ his​ ​ moves​ ​ and​ ​ will​ ​ use​ ​ a
simple​ ​ program​ ​ to​ ​ determine​ ​ where​ ​ the​ ​ ball​ ​ is.​ ​ Write​ ​ that​ ​ program.
'''
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
            shuffle_me = int(input('How many time should the cups be shuffled: ')) # ask user how many times should be shuffled
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
        print('Position of the ball is: {}'.format(cups)) # Show the ball position inside list
        print()
        print('The ball is under the FIRST cup')
    elif cups[1] == 'X':
        print()
        print('Position of the ball is: {}'.format(cups))
        print()
        print('The ball is under the SECOND cup')
    else:
        print()
        print('Position of the ball is: {}'.format(cups))
        print()
        print('The ball is under the THIRD cup')

while True: # plays
    swap_the_cups()
    print()

    play_again = input('Play again? (Y/n): ')
    
    if play_again.lower() != 'n':
        continue
    else:
        sys.exit()