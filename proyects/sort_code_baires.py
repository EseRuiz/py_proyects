def sort_code(code):
    list_sort = list(code)
    order_list = sorted(list_sort)
    str_list = ''.join(order_list)
    return str_list

a = sort_code("cbaja")
print(a)