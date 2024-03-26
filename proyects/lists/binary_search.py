def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")
    ind = search_list.index(value)
    return ind