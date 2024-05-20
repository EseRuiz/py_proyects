# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"


def score(dice, category):
    num = {nam: dice.count(nam) for nam in dice}

    if category in (ONES,TWOS,THREES,FOURS,FIVES,SIXES):
        return num.get(category, 0) * category
    #     return num[category]*category
    # elif category in (ONES,TWOS,THREES,FOURS,FIVES,SIXES) and category not in dice:
    #     return 0
    if category == YACHT:
        if 5 in num.values():
            return 50
        else:
            return 0
        
    if category == FULL_HOUSE:
        total = 0
        if 3 in num.values() and 2 in num.values():
            for k , v in num.items():
                total += k*v
            return total
        else:
            return 0
        
    if category == FOUR_OF_A_KIND:
        total = 0
        if 5 in num.values():
            for k , v in num.items():
                if v == 5:
                    total += k*4
                    return total
        if 4 in num.values():
            for k , v in num.items():
                if v == 4:
                    total += k*v
            return total
        else:
            return 0   
        
    if category == LITTLE_STRAIGHT:
        dice.sort()
        if dice == [1,2,3,4,5]:
            return 30
        else:
            return 0 
        
    if category == BIG_STRAIGHT:
        dice.sort()
        if dice == [2,3,4,5,6]:
            return 30
        else:
            return 0 

    if category == CHOICE:
        total = 0
        for k , v in num.items():
            total += k*v
        return total
        
# a = score([3, 3, 3, 3, 3], FOUR_OF_A_KIND)
# print(a)