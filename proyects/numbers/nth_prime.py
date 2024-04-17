def prime(number):
    if number <= 0 :
        raise ValueError('there is no zeroth prime')
    primes = []
    num = 2
    while len(primes) < number:
        is_prime = True
        for prime_num in primes:
            if num % prime_num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes[-1] 

#a = prime(10001)  
#print(a)
