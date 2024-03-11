first_number = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
decimals = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",
            18:"eighteen",19:"nineteen",20:"twenty",30 : 'thirty', 40 : 'forty', 50 : 'fifty',60 : 'sixty',
            70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
centcimals = {1:"hundred",2:"thousand",3:"million",4:"billion"}

def say(number):
    if number < 0 or len(str(number)) > 12:
        raise ValueError("input out of range")
    if number == 0:
        return first_number[0]
    
    conta = 1
    total = []
    while number > 0:
        num = ''
        numb = number % 1000
        if numb >= 100:
            num += first_number[numb//100]+' '+ centcimals[1]+' '
            numb %= 100

        if numb >= 10 and numb <= 19:
            num += decimals[numb] + ' '
            numb = 0

        if numb >= 20:
            num += decimals[(numb//10)*10]
            if numb % 10 != 0:
                num += '-'
            numb %= 10

        if numb > 0:
            num += first_number[numb]+' '

        if num.strip() and conta > 1:
            num += centcimals[conta] + ' '

        total.append(num.strip())
        conta += 1
        number //= 1000
        
    return ' '.join(total[::-1]).strip()


a = say(14)
print(a)