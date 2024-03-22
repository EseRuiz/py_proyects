def answer(question):
    operations = ["plus","minus","multiplied","divided"]
    words = question.split()
    res = 0

    if words[0] == "What" and words[0] == "is" and len(words) == 2:
        return words[2].strip('-').strip("?")
    if len(words) == 2:
        raise ValueError("syntax error")
    if words[-1].strip('-').strip("?") in operations:
        raise ValueError("syntax error")
    if len(words) > 4 and words[2] in operations:
        raise ValueError("syntax error")
    if len(words) > 4 and words[4] in operations and str(words[-1]).strip('-').strip("?").isnumeric():
        raise ValueError("syntax error")
    if len(words) > 4 and str(words[-2]).strip('-').strip("?").isnumeric() and str(words[-1]).strip('-').strip("?").isnumeric():
        raise ValueError("syntax error")

    elif len(words)>3 and words[3] not in operations or words[0] != "What":
        raise ValueError("unknown operation")
    else:
        if "?" in words[2] :
            number = [num for num in words[2]]
            res = int(number[0])
        if len(words)>3 and words[3] == "plus":
            res = (int(words[2])+int(words[4].strip("?")))
        if len(words)>3 and words[3] == "minus":
            res = (int(words[2])-int(words[4].strip("?")))
        if len(words)>3 and words[3] == "multiplied":
            res = (int(words[2])*int(words[5].strip("?")))
        if len(words)>3 and words[3] == "divided":
            res = (int(words[2])/int(words[5].strip("?")))
    
        if len(words) > 5 and len(words) < 9:
            print(res,len(words) > 6 and words[5] in operations)
            if words[5] in ["plus","minus"]:
                if words[5] == "plus":
                    return res + int(words[6].strip("?"))
                elif words[5] == "minus":
                    return res - int(words[6].strip("?"))
            elif len(words) > 6 and words[5] in operations:
                if words[5] == "multiplied":
                    return res * int(words[-1].strip("?"))
                elif words[5] == "divided":
                    return res / int(words[-1].strip("?"))
                
        if len(words) > 8 and len(words) < 10:
            print("hola")
            if words[5] in operations:
                if words[5] == "plus":
                    return res + int(words[6].strip("?"))
                elif words[5] == "minus":
                    return res - int(words[6].strip("?"))
            elif len(words) > 6 and words[6] in operations:
                if words[6] == "multiplied":
                    return res * int(words[-1].strip("?"))
                elif words[6] == "divided":
                    return res / int(words[-1].strip("?"))
        
    return int(res)
    

    
a = answer("What is -3 plus 7 multiplied by -2?")
print(a)