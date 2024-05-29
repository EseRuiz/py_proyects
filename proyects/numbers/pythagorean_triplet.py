def triplets_with_sum(number):
    res = []
    a_init = 1
    for a in range(a_init,int(number/3)):
        for b in range (a+1,int((number-a_init)/2)):
            c = number - a - b
            if (a**2)+(b**2) == (c**2) :
                res.append([a,b,c])
                a_init = a
    return res
a = triplets_with_sum(30000)
print(a)