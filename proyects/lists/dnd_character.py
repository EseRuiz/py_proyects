from random import randint

def modifier(num):
    return (num-10)//2

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        values = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
        values.remove(min(values))
        return sum(values)
