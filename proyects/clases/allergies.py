ALLERGIES = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}
class Allergies:
    lst_res = []
    
    def __init__(self, score):
        self.score = score
        
    def allergic_to(self, item):
        self.item = item 
        if self.score & ALLERGIES[self.item] > 0: 
            return True
        return False

    @property
    def lst(self):
        self.lst_res =[aller for aller in ALLERGIES.keys() if self.allergic_to(aller)]
        return self.lst_res
    
# print(Allergies(5).allergic_to("peanuts"))
# print(Allergies(5).lst, ["peanuts"])

Si self.score fuera 5 (binario 0101) y ALLERGIES[self.item] fuera 2 (binario 0010), la operación sería:

# 0101 (5)
# & 0010 (2)
# ------
# 0000 (0)