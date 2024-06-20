num = {"0":[" _ ", "| |", "|_|", "   "],
       "1":["   ", "  |", "  |", "   "],
       "2":[" _ ", " _|", "|_ ", "   "],
       "3":[" _ ", " _|", " _|", "   "],
       "4":["   ", "|_|", "  |", "   "],
       "5":[" _ ", "|_ ", " _|", "   "],
       "6":[" _ ", "|_ ", "|_|", "   "],
       "7":[" _ ", "  |", "  |", "   "],
       "8":[" _ ", "|_|", "|_|", "   "],
       "9":[" _ ", "|_|", " _|", "   "]}

def convert(input_grid):

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    result_parts = []
    res = ""

    # Procesar cada segmento de 4 filas en pasos de 4 en 4
    for k in range(0, len(input_grid), 4):
        segment = input_grid[k:k+4]
        rows = ["", "", "", ""]

        for i in range(4):
            rows[i] = segment[i]

        # Generar columnas de 3 caracteres a partir de las filas reestructuradas
        #en paso de 3 en 3
        col = []
        for i in range(0, len(rows[0]), 3):
            digit = [row[i:i+3] for row in rows]
            col.append(digit)

        for col_val in col:
            
            exist = False

            for col_v_len in col_val:
                if len(col_v_len) != 3:
                    raise ValueError("Number of input columns is not a multiple of three")

            for key, value in num.items():
                if col_val == value:
                    res += key
                    exist = True
                    break
            if not exist:
                res += "?"

        result_parts.append(res)
        res = ""

    return ",".join(result_parts) if len(result_parts) > 1 else result_parts[0]


# test = [
#         "    _  _ ",
#         "  | _| _|",
#         "  ||_  _|",
#         "         ",
#         "    _  _ ",
#         "|_||_ |_ ",
#         "  | _||_|",
#         "         ",
#         " _  _  _ ",
#         "  ||_||_|",
#         "  ||_| _|",
#         "         ",
#     ]
# a = convert(test)
# print(a)
