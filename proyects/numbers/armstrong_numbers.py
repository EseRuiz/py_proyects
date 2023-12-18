def is_armstrong_number(number):
    is_arm_nu_val = False
    value = 0
    digito =[int(n) for n in str(number)]
    for nu in digito:
        value += int(nu)**(len(str(number)))
    if value == number:
        is_arm_nu_val = True
    return is_arm_nu_val


