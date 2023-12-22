def response(hey_bob):
    list_num=hey_bob.replace(",","")
    if "?" in hey_bob and hey_bob.upper()==hey_bob and len(hey_bob)>4:
        return ("Calm down, I know what I'm doing!")
    elif hey_bob.strip().endswith("?"):
        return ("Sure.")
    elif hey_bob.isspace() or "" == hey_bob:
        return("Fine. Be that way!")
    elif hey_bob.upper() == hey_bob and not hey_bob.isspace() and list_num.replace(" ","").isnumeric() == False:
        return("Whoa, chill out!")
    elif hey_bob.isnumeric():
        return("Whatever.")
    return("Whatever.")