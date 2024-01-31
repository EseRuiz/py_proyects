def resistor_label(colors):
    multiplier = ""
    multiplier5 = ""
    tolerancia = {'grey':0.05 ,'violet' :0.1,'blue':0.25, 'green':0.5,'brown': 1,'red': 2,'gold':5,'silver':10}
    dictionary = {'black':0,'brown': 1,'red': 2,'orange': 3,'yellow': 4,'green': 5,'blue': 6,'violet': 7,'grey': 8,'white': 9}
    if colors[0] == 'black':
        return "0 ohms"
    if len(colors)==4:
        val= (str(dictionary[colors[0]]),str(dictionary[colors[1]]))
        value = "".join(val)
        if int(dictionary[colors[0]]) == 0 and int(dictionary[colors[2]]) == 0:
            multiplier = " ohms " 
            return str(dictionary[colors[1]])+multiplier
        if int(dictionary[colors[2]]) == 0:
            multiplier = " ohms"
        if int(dictionary[colors[2]]) == 1:
            multiplier = "0 ohms"
        if int(dictionary[colors[2]]) == 2:
            if int(dictionary[colors[1]]) == 0:
                aux = (str(dictionary[colors[0]]))
                aux = "".join(aux)
                multiplier = " kiloohms"+' ±'+str(tolerancia[colors[3]])+'%'
                return aux+multiplier
            aux = (str(dictionary[colors[0]]),'.',str(dictionary[colors[1]]))
            aux = "".join(aux)
            multiplier = " kiloohms"+' ±'+str(tolerancia[colors[3]])+'%'
            return aux+multiplier
        if int(dictionary[colors[2]]) == 3:
            multiplier = " kiloohms"
        if int(dictionary[colors[2]]) == 4:
            multiplier = "0 kiloohms "
        if int(dictionary[colors[2]]) == 6:
            multiplier = " megaohms "
        if int(dictionary[colors[2]]) == 9:
            multiplier = " gigaohms "
        return value+multiplier+' ±'+str(tolerancia[colors[3]])+'%'
    if len(colors)==5:
        if int(dictionary[colors[3]]) == 0:
            val5= (str(dictionary[colors[0]]),str(dictionary[colors[1]]))
            value5 = "".join(val5)
            multiplier = " ohms ±"
            return value5+str(dictionary[colors[2]])+multiplier+str(dictionary[colors[4]])+'%'
        if int(dictionary[colors[3]]) == 1:
            val5= (str(dictionary[colors[0]]),'.',str(dictionary[colors[1]]),str(dictionary[colors[2]]))
            value5 = "".join(val5)
            multiplier =value5+ " kiloohms ±"
        if int(dictionary[colors[3]]) == 2:
            val5= (str(dictionary[colors[0]]),str(dictionary[colors[1]]),'.',str(dictionary[colors[2]]))
            value5 = "".join(val5)
            multiplier =value5+ " kiloohms ±"
        if int(dictionary[colors[3]]) == 3:
            val5= (str(dictionary[colors[0]]),str(dictionary[colors[1]]),str(dictionary[colors[2]]))
            value5 = "".join(val5)
            multiplier =value5+ " kiloohms ±"
        if int(dictionary[colors[3]]) == 4:
            val5= (str(dictionary[colors[0]]),'.',str(dictionary[colors[1]]),str(dictionary[colors[2]]))
            value5 = "".join(val5)
            multiplier =value5+ " megaohms ±"
        if int(dictionary[colors[3]]) == 5:
            val5= (str(dictionary[colors[0]]),str(dictionary[colors[1]]),'.',str(dictionary[colors[2]]))
            value5 = "".join(val5)
            multiplier =value5+ " megaohms ±"
        if int(dictionary[colors[3]]) == 6:
            val5= (str(dictionary[colors[0]]),str(dictionary[colors[1]]),'.',str(dictionary[colors[2]]))
            value5 = "".join(val5)
            multiplier =value5+ " megaohms ±"
        if int(dictionary[colors[3]]) == 7:
            val5= (str(dictionary[colors[0]]),str(dictionary[colors[1]]),str(dictionary[colors[2]]))
            value5 = "".join(val5)
            multiplier =value5+ " megaohms ±"
        return multiplier+str(tolerancia[colors[4]])+'%'


    
a = resistor_label(["brown", "red", "orange", "green", "blue"])
print(a)
#TODO do a better algorythm about count decimals, and put de point (.)
