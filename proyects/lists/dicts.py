"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    new_dict = {llave: items.count(llave) for llave in items}
    return new_dict


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for key,value in inventory.items():
        for val in range(value):
            items.append(key)
    new_dict = {llave: items.count(llave) for llave in items}
    return new_dict


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    new_dict = {llave: items.count(llave) for llave in items}
    for key,val in new_dict.items():
        if key in inventory:
            inventory[key]-=val
        pass
    for key,val in inventory.items():
        if val < 0:
            inventory[key]=0
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    new_item = [item]
    for key in new_item:
        if key in inventory.keys():
            inventory.pop(key)
    return inventory



def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    print(inventory)
    new_inventory = {llave:valor for llave,valor in inventory.items() if valor > 0}
    print(new_inventory)
    new_inventory = list(new_inventory.items())
    return new_inventory#TODO CREAR DICCIONARIO JSON

a = create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
b = add_items({"wood": 2, "gold": 1, "diamond": 3}, ["wood", "gold", "gold"])
c = decrement_items({"wood": 2, "iron": 3, "diamond": 1},["wood", "wood", "wood", "iron", "diamond", "diamond"])
d = remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood")
e = list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
print(e)