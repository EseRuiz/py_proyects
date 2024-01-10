import re
def is_valid(isbn):
    res = 0
    new_isbn = re.sub('-','',isbn).replace(' ', '').upper()
    if len(new_isbn) != 10 or 'X' in new_isbn and new_isbn[len(new_isbn)-1] != 'X':
        return False
    ct = re.sub(r'[^Xx0-9]', '', isbn).upper().replace('-', '')
    arr_ct = [10 if num == 'X' else float(num) for num in ct ]
    flag = 10
    for nn in arr_ct:
        res += nn * flag
        flag -= 1
    if res % 11 == 0  and len(arr_ct) == 10:
        return True
    return False


