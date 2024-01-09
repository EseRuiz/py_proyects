def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    list_div = [num for num in range(1,number) if number % num == 0  ]
    print(list_div,sum(list_div))
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == sum(list_div):
        return("perfect")
    if number < sum(list_div):
        return("abundant")
    if number > sum(list_div):
        return("deficient")