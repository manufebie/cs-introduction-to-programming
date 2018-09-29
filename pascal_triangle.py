'''
Pascal Triangle

Since I don't really understand how to convert the Pascal Triangle into
code. I had to use some help from Youtube/Google.

Source: https://www.youtube.com/watch?v=AseArgEwCzI
'''
import os, sys


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_pascal(x):
    clear()
    if x == 0:
        return []
    elif x == 1:
        return [[1]]
    else:
        new_row = [1]
        result = generate_pascal(x-1)
        last_row = result[-1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
        return result

while True:
    clear()

    print('Enter a number to generate a Pascal Triangle: \n')
    x = int(input('> '))

    pascal_triangle = generate_pascal(x)

    for i in range(len(pascal_triangle) -1):
        print(pascal_triangle[i])

    print()
    play_again = input('Play again? (Y/n): ')

    if play_again != 'n':
        pascal_triangle
    else:
        clear()
        sys.exit()