def sum_of_multiples(limit, multiples):
    valist = []
    for num in multiples:
        if num == 0:
            valist.append(0)
            break
        for val in range(limit):
            if val % num == 0:
                valist.append(val)
    vaset = set(valist)
    result = sum(vaset)
    return result
a = sum_of_multiples(1000, [3, 5])
print(a)
#233168