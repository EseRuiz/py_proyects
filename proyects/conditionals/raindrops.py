def convert(number):
    total = ""
    tres = ""
    cinco = ""
    siete = ""
    if(number % 3 != 0 and number % 5 != 0 and number % 7 != 0):
        return str(number)
    if(number % 3 == 0 ):
        tres = "Pling"
    if(number % 5 == 0 ):
        cinco = "Plang"
    if(number % 7 == 0 ):
        siete = "Plong"
    return (tres + cinco + siete)