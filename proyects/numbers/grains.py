def square(number):
    var_result = 2**(number-1)
    if (number <= 0 or number > 64) :
        raise ValueError("square must be between 1 and 64")
    return var_result

 
def total():
    var_acum = 0
    for num in range(1,65):
        var_acum += (2**(num-1))
    return var_acum
    

