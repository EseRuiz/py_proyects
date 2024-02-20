
cuadrados = [(int(a)**2) for a in range (1,101) ]
pares = [ par for par in range(1,21) if par % 2 == 0]
impares = [impar for impar in range (1,21) if impar % 2 != 0]
a = [uno for uno in range (1,8)]
b = [dos for dos in range (3,11)]
solo_lista = [ una for una in a if una in b]
solo_lista_dif = [ una for una in a if una not in b]


sta = "hello"
stb = "world"

strin_list = [ st for st in sta if st in stb]

impares_cuad = [(int(im)**2) for im in range (1,101) if im % 2 != 0]

set_list = {num for num in range (1,11) if  num % 3 == 0}

var = "3598-21507X"

arr_ct = ['10' if num == 'X' else num for num in var ]
##['3', '5', '9', '8', '2', '1', '5', '0', '7', '10']

tuples = [('a', 1), ('b', 2), ('c', 3)]

dict_tuple = {llave : valor for llave,valor in tuples if llave == 'b' }

name  = 'example'

dict_word = { letra : name.count(letra) for letra in name}

prueba =[
    {
     "name":"papa",
     "apellido":"pastusa",
     "ensalada":False
    },
    {
     "name":"papa",
     "apellido":"sabanera",
     "ensalada":True
    },
    {
     "name":"papa",
     "apellido":"criolla",
     "ensalada":True
    },
    {
     "name":"papa",
     "apellido":"ibia",
     "ensalada":False
    },
    {
     "name":"papa",
     "apellido":"francesa",
     "ensalada":True
    }
]

list1 = [var for var in prueba if var["ensalada"]==True]
list2 = [var for var in prueba if var["ensalada"]==False]

