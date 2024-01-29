def label(colors):
    multiplier = ""
    dictionary = {'black':0,'brown': 1,'red': 2,'orange': 3,'yellow': 4,'green': 5,'blue': 6,'violet': 7,'grey': 8,'white': 9}
    val= (str(dictionary[colors[0]]),str(dictionary[colors[1]]))
    value = "".join(val)
    if int(dictionary[colors[0]]) == 0 and int(dictionary[colors[2]]) == 0:
        multiplier = " ohms" 
        return str(dictionary[colors[1]])+multiplier
    if int(dictionary[colors[2]]) == 0:
        multiplier = " ohms"
    if int(dictionary[colors[2]]) == 1:
        multiplier = "0 ohms"
    if int(dictionary[colors[2]]) == 2:
        multiplier = " kiloohms"
        return str(dictionary[colors[0]])+multiplier
    if int(dictionary[colors[2]]) == 3:
        multiplier = " kiloohms"
    if int(dictionary[colors[2]]) == 4:
        multiplier = "0 kiloohms"
    if int(dictionary[colors[2]]) == 6:
        multiplier = " megaohms"
    if int(dictionary[colors[2]]) == 9:
        multiplier = " gigaohms"
    return value+multiplier

a = label(["red", "black", "red"])
print(a)
