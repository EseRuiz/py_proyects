def translate(text):
    res = []
    final_word=""
    first_list=['a','e','i','o','u','xr','yt']
    consonants_list=['p', 'q', 'b', 't', 'd', 'c', 'j', 'k', 'g', 'f', 'v', 's', 'z', 'm', 'n', 'ñ', 'l', 'x', 'r', 'w', 'e', 'y', 'h']
 
    new_text = new_text = [word for word in text.split() if word.strip()]
    
    for words in new_text:
        word = [n for n in words]
        print(word)
        if word[0] in first_list or word[0]+word[1] in first_list :
            return  text + "ay"
        
        if word[1] == "y":
            word[1]="ay"
            for f in word:
                final_word += f
            return  ("y"+final_word)
        
        if (word[0] in consonants_list 
            and word[0]+word[1] != "ch" 
            and word[0]+word[1] != "sc" 
            and word[0]+word[1] != "qu" 
            and word[0]+word[1] != "sq"
            and word[0]+word[1] != "th"
            and word[0]+word[1] != "rh"):
            final_word=""
            flag=word[0]
            word[0]=""
            for f in word:
                final_word += f
            result = (final_word+flag+"ay")

        if word[0]+word[1]=="ch":
            word[0]=""
            word[1]=""
            for f in word:
                final_word += f
            result = final_word+"ch"+"ay"
        
        if word[0]+word[1]+word[2] == "sch":
            word[0]=""
            word[1]=""
            word[2]=""
            for f in word:
                final_word += f
            result = (final_word+"sch"+"ay")
        
        if word[0]+word[1]+word[2] == "thr":
            word[0]=""
            word[1]=""
            word[2]=""
            for f in word:
                final_word += f
            result = (final_word+"thr"+"ay")
        
        if word[0]+word[1]=="qu":
            word[0]=""
            word[1]=""
            for f in word:
                final_word += f
            result = (final_word+"qu"+"ay")
        
        if word[0]+word[1]=="th":
            word[0]=""
            word[1]=""
            for f in word:
                final_word += f
            result = (final_word+"th"+"ay")
        
        if word[0]+word[1]+word[2] == "squ":
            word[0]=""
            word[1]=""
            word[2]=""
            for f in word:
                final_word += f
            result = (final_word+"squ"+"ay")
        
        if word[0] == "y":
            word[0]=""
            for f in word:
                final_word += f
            result = (final_word+"y"+"ay")
        
        if word[0]+word[1] == "rh" and word[2] == "y":
            word[0]=""
            word[1]=""
            for f in word:
                final_word += f
            result = (final_word+"rhay")

        res.append(result)
    res = ' '.join(res)
    return res
