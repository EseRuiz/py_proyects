import re
def is_isogram(string):
    ct = re.sub(r'[^a-zA-Z]', '', string).upper().replace(' ', '')
    set_count = [ct.count(letra) for letra in ct ]
    for nun in set_count:
        if nun > 1:
            return False
    return True

