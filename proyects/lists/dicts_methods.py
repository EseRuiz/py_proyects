"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    list_item = list(items_to_add)
    dict_item = {llave: list_item.count(llave) for llave in list_item}
    for key,value in dict_item.items():
        if key in current_cart.keys():
            current_cart[key] += value
        else :current_cart[key]=value
    return (current_cart)
 


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    list_item = list(notes)
    dict_item = {llave: list_item.count(llave) for llave in list_item}
    return dict_item


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas
    


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    val =dict(sorted(cart.items()))
    return val


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    for key in cart.keys():
        for key2 in aisle_mapping.keys():
            if key == key2:
                aisle_mapping[key2].insert(0,cart[key])
    sorted_items = sorted(aisle_mapping.items(), reverse=True)
    sorted_dict = dict(sorted_items)
    
    return sorted_dict


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key in store_inventory.keys():
        for ke2 in fulfillment_cart.keys():
            if key == ke2:
                store_inventory[key][0] -= fulfillment_cart[ke2][0]
                if store_inventory[key][0] <= 0:
                    store_inventory[key][0] = 'Out of Stock'

    return store_inventory

a = add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
              ['Banana', 'Orange', 'Blueberries', 'Banana'])
b = update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Eggs': 3},
                  'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
                (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),))
c = send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
                  {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]})
d = update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True],
                  'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
                 {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False],
                  'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}),
print(d)