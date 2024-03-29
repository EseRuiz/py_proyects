"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if (list_one == [] and list_two != []):
        return SUBLIST
    if (list_two == [] and list_one != []):
        return SUPERLIST
    if len(list_one) < len(list_two) and list_one[0] in list_two:
        idx = list_two.index(list_one[len(list_one)-1])
        new_list = list_two[idx-len(list_one)+1 : idx+1]
        if new_list == list_one :
            return SUBLIST
        return UNEQUAL
    if len(list_one) > len(list_two):
        idy = list_one.index(list_two[len(list_two)-1])
        new_list2 = list_one[idy-len(list_two)+1 : idy+1]
        if new_list2 == list_two :
            return SUPERLIST
        return UNEQUAL
    return UNEQUAL

    
