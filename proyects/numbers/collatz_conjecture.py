def steps(number):
    n = 0
    var = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    elif number == 1:
        return n
    else:
        while var != 1:
            if number % 2 == 0:
                var = int(number / 2)
                n += 1
            if number % 2 != 0:
                var = int((number * 3)+1)
                n += 1
            number = var
            if var == 1:
                return n
