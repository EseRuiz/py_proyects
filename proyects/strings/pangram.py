import re
def is_pangram(sentence):
    ct = re.sub(r'[^a-zA-Z]', '', sentence).upper().replace(' ', '')
    set_ct = {se for se in ct}
    list_ct = sorted(list(set_ct))
    if len(list_ct) == 26 :
        return True
    return False

