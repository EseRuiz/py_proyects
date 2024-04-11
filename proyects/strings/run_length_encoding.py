def decode(string):
    res = ""
    acum_num = ""
    for num in string:
        if num.isnumeric():
            acum_num += num
        else:
            if acum_num: 
                res += int(acum_num) * num
                acum_num = ""
            else:
                res += num
    return res

def encode(string):
    count = 1
    res = ""
    if string == "":
        return string
    acum = string[0]
    for letter in string[1:]:
        if acum == letter:
            count += 1
        else:
            if count == 1:
                res +=  acum 
                acum = letter
                count = 1
            else:
                res += str(count) + acum 
                acum = letter
                count = 1
    if count == 1:
        res +=  acum 
    else:
        res += str(count) + acum 
    return res

a = encode("XYZ")
b = decode("12WB12W3B24WB")
print(a)
