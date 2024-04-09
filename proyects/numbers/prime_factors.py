def factors(value):
    result = []
    num = 2
    val = value
    while num <= val:
        #print(val, num)
        if val % num == 0 :
            result.append(num)
            val = val // num
            num = 1
        num += 1
    return result
a = factors(93819012551)
print(a)