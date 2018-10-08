'''
1) KMP
Great​ ​ scientific​ ​ discoveries​ ​ are​ ​ often​ ​ named​ ​ by​ ​ the​ ​ last​ ​ names​ ​ of
scientists​ ​ that​ ​ made​ ​ them.​ ​ For​ ​ example,​ ​ the​ ​ most​ ​ popular​ ​ asymmetric
cryptography​ ​ system,​ ​ RSA​ ​ was​ ​ discovered​ ​ by​ ​ Rivest,​ ​ Shamir​ ​ and
Adleman.​ ​ Another​ ​ notable​ ​ example​ ​ is​ ​ the​ ​ Knuth-Morris-Pratt​ ​ algorithm,
named​ ​ by​ ​ Knuth,​ ​ Morris​ ​ and​ ​ Pratt.

Scientific​ ​ papers​ ​ reference​ ​ earlier​ ​ works​ ​ a ​ ​ lot​ ​ and​ ​ it’s​ ​ not​ ​ uncommon​ ​ for
one​ ​ document​ ​ to​ ​ use​ ​ two​ ​ different​ ​ naming​ ​ conventions:​ ​ the​ ​ short
variation​ ​ (e.g.​ ​ KMP)​ ​ using​ ​ only​ ​ the​ ​ first​ ​ letters​ ​ of​ ​ authors​ ​ last​ ​ names​ ​ and
the​ ​ long​ ​ variation​ ​ (e.g.​ ​ Knuth-Morris-Pratt)​ ​ using​ ​ complete​ ​ last​ ​ names
separated​ ​ by​ ​ hyphens.

We​ ​ find​ ​ mixing​ ​ two​ ​ conventions​ ​ in​ ​ one​ ​ paper​ ​ to​ ​ be​ ​ aesthetically
unpleasing​ ​ and​ ​ would​ ​ like​ ​ you​ ​ to​ ​ write​ ​ a ​ ​ program​ ​ that​ ​ will​ ​ transform​ ​ long
variations​ ​ into​ ​ short.
'''
import os

# ask user to input full name
# grab the first letter of each name
# display the firstletter

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def name_transform():
    clear()
    hyphen_check = ('-') 
    print('Type the last names of some persons')
    print('Seperate the lastnames with hypens. For example: Kent-Wayne-Queen\n')
    while True:
        names = input('> ')
        if hyphen_check not in names: # checks if the input contains a hyphen or not
            clear()
            print('Make sure you seperate the names with a hypen "-"!!') # Remind user to seperate names with hyphen
            print('Try again\n') 
        else:
            split_names = names.split('-') # split the string by hyphen
            break

    print('> Result: ', end='')
    for i in split_names: # loop over the list of inserted names
        names = i[0].upper() # turn each first letter into upper
        print(names, end='')
    print()


name_transform()
