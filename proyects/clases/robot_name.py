import random

dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class Robot:
    name = ""
    name2 = ""
    def __init__(self):
        self.name = ''.join(random.choices(dictionary,k=2)).upper() + str(random.randrange(100,999))

    def reset(self):
        random.seed()
        self.name = ''.join(random.choices(dictionary,k=2)).upper() + str(random.randrange(100,999))
        return self.name
    
