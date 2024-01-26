def rebase(input_base, digits, output_base):
    longitud_name = 0
    total = 0
    final_data = []
    if input_base < 2 :
        raise ValueError("input base must be >= 2")
    for dig in digits:
        if dig < 0 or dig >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2 :
        raise ValueError("output base must be >= 2")
    
    longitud_name = len(digits)-1
    for number in digits:
        print(number,input_base,longitud_name)
        total += (number* (input_base**longitud_name))
        longitud_name -= 1
    if total == 0:
        return [0]
    

    while total != 0:
        final_data.insert(0,total%output_base)
        total = total // output_base
    return final_data

#a = rebase(97, [3, 46, 60], 73)
#print(a)
    