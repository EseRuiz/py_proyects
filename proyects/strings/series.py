def slices(series, length):
    resul = []
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if series == "":
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    for val in range(len(series)):
        if len(series[val:length+val]) == length:
            resul.append(series[val:length+val])
    return resul

a = slices("9142", 2)
print(a)