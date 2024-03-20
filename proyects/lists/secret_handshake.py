def commands(binary_str):
    res =[]
    list_numbers = [num for num in binary_str]
    if list_numbers[4] == '1':
        res.append('wink')
    if list_numbers[3] == '1':
        res.append('double blink')
    if list_numbers[2] == '1':
        res.append('close your eyes')
    if list_numbers[1] == '1':
        res.append('jump')
    if list_numbers[0] == '1':
        res.reverse()
    return res
    

a = commands("11010")
print(a)
