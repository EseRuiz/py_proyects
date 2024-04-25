def square_of_sum(number):
    #val = [num for  num in range(1,number+1)]
    val = ((number * (number + 1)) / 2) **2
    
    return (int(val))

def sum_of_squares(number):
    #val = [num**2 for num in range(1,number+1)]
    val = (number * (number + 1) * (2 * number + 1)) / 6
    return (int(val))

def difference_of_squares(number):
    return square_of_sum(number)-sum_of_squares(number)

a = square_of_sum(5)
b = sum_of_squares(5)
print(b)