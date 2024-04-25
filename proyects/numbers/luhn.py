import re
class Luhn:
    def __init__(self, card_num):
        self.card = card_num

    def valid(self):
        res = []
        solo_numeros = ''.join(self.card.split())
        if not solo_numeros.isdigit() or solo_numeros == "0":
            return False
        lis_numeros = [int(num) for num in solo_numeros]
        rev_lis = list(reversed(lis_numeros))
        for i in range(len(rev_lis)):
            if i%2 != 0:
                con = rev_lis[i]*2
                if con > 9:
                    con -= 9
                res.append(con)
            else:
                res.append(rev_lis[i])
        print(sum(res))
        return (sum(res)%10==0)



a = Luhn("055# 444$ 285").valid()
print(a==True)