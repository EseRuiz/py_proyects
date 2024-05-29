def primes(limit):
    result = {}
    conta = 0
    for num in range(2,limit+1):
        for nn in range (2,limit+1):
            #print(num , nn ,num % nn == 0)
            if num > 1 and num % nn == 0:
                conta +=1
            if conta == 1 and nn == limit:
                result[num]="none"
                conta = 0
            if conta > 1:
                result[num]="no_prim"
                conta = 0
                break
    list_result = [k for k,v in result.items() if v == "none"]
    return list_result
#TODO que al detectar un numero none, sus multiplos los descarte de una vez y no los vuelva a mirar
#optimizando tiempo
a = primes(10)
print(a)