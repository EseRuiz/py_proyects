class PhoneNumber:
    num = ""
    def __init__(self, number):
        num = number.replace(".","").replace("-","").replace(" ","").replace("(","").replace(")","").replace("+","")
        if any(caracter.isalpha() for caracter in num):
            raise ValueError("letters not permitted")
        for nu in num:
            if nu in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
                raise ValueError("punctuations not permitted")
        if len(num) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(num) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(num) == 11 and num[0] != "1":
            raise ValueError("11 digits must start with 1")
        if len(num) == 10 and num[0] == "0" or len(num) == 11 and num[1] == "0":
            raise ValueError("area code cannot start with zero")
        if len(num) == 10 and num[0] == "1" or len(num) == 11 and num[1] == "1":
            raise ValueError("area code cannot start with one")
        if len(num) == 10 and num[3] == "0" or len(num) == 11 and num[4] == "0":
            raise ValueError("exchange code cannot start with zero")
        if len(num) == 10 and num[3] == "1" or len(num) == 11 and num[4] == "1":
            raise ValueError("exchange code cannot start with one")

        if len(num) == 11:
            self.number = num[1:11]
        else: self.number = num

        self.area_code = self.number[0:3]

    def pretty(self):
        self.number = f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6::]}"
        return self.number




#num = PhoneNumber("523-@:!-7890").number
#print(num)