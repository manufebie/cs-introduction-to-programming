'''
-> Sell pets
-> Buy pets
-> View pets
'''

class Animal:

    def __init__(self, specie):
        self.specie = specie

    def __str__(self):
        return self.specie


class PetShop:

    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_pet(self, name): 
        animal = Animal(name)
        self.animals.append(animal)
    
    def del_pet(self, index):
        # remove animal from list
        self.animals.pop(index)

    def diplay_pets(self):
        for index, animal in enumerate(self.animals):
            print('--> [{}] {}'.format(index, animal))
