from functools import reduce

def append(list1, list2):
    lis = []
    if list1 == [] and list2 == []:
        return lis
    if list1 == []:
        return list2
    if list2 == []:
        return list1
    if list1 != [] and list2 != []:
        for li in list2:
            list1.append(li)
        return list1


def concat(lists):
    list_new = []
    for lis in lists:
        list_new += lis
    return list_new


def filter(function, lst):
    if lst == []:
        return []
    fun = [num for num in lst if function(num)]
    return fun


def length(lst):
    if lst == []:
        return 0
    longitud = len(lst)
    return longitud

def map(function, lst):
    fun =[]
    if lst == []:
        return []
    for li in lst:
        fun.append(function(li))
    return fun


def foldl(function, lst, initial):
    if lst == []:
        return initial
    fun = reduce(function,lst,initial)
    return fun


def foldr(function, lst, initial):
    if lst == []:
        return initial
    fun = reduce(function,lst[::-1],initial)
    return fun


def reverse(list):
    return list[::-1]

a = append([1, 2], [2, 3, 4, 5])
b = concat([[1, 2], [3], [], [4, 5, 6]])
c = map(lambda x: x + 1, [1, 3, 5, 7])
print(c)