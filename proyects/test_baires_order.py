def ranks(arr):
    arr2 = list(set(arr))
    sort_array = sorted(arr2, reverse=True)
    dict_array = {sort_array[i]: i+1 for i in range(len(sort_array))}
    res = [ dict_array.get(i) for i in arr]

    return res

a = ranks([3,3,3,3,3,5,1])
print(a)