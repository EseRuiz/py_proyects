def roman(number):
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    miles = ["", "M", "MM", "MMM"]

    miles_str = miles[number // 1000]
    centena = centenas[(number % 1000) // 100]
    decenta = decenas[(number % 100) // 10]
    unidad = unidades[number % 10]

    return miles_str + centena + decenta + unidad

#a = roman(1024)
#print(a)  # Salida: MXXIV

