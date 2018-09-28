'''
2) Modulo 42

Given​ ​ two​ ​ integers​ ​ A ​ ​ and​ ​ B , ​ ​ ​ A ​ ​ modulo​ ​ B ​ ​ is​ ​ the​ ​ remainder​ ​ when​ ​ dividing
A ​ ​ by​ ​ B ​ . ​ ​ For​ ​ example,​ ​ the​ ​ numbers​ ​ 7,​ ​ 14,​ ​ 27​ ​ and​ ​ 38​ ​ become​ ​ 1,​ ​ 2,​ ​ 0 ​ ​ and
2,​ ​ modulo​ ​ 3.​ ​ Write​ ​ a ​ ​ program​ ​ that​ ​ accepts​ ​ 10​ ​ numbers​ ​ as​ ​ input​ ​ and
outputs​ ​ the​ ​ number​ ​ of​ ​ distinct​ ​ answers​ ​ from​ ​ the​ ​ input​ ​ modulo​ ​ by​ ​ 42.
''' 

print('Enter 10 numbers: \n') # ask user to inpur an integer 10 x
_ = 0

while _ < 10:
    _ += 1
    # try/except block to check if user enters an integer
    try:
        x = int(input('> '))
    except ValueError:
        print('Only positive numbers allowed')
        _ -= 1 # goes on step back and continues
        continue
    y = x % 42

