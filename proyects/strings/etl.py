def transform(legacy_data):
    data = {}
    for key,val in legacy_data.items():
        for new_val in val:
            data[new_val.lower()] = key
    sort_data = dict(sorted(data.items()))
    sort_data
    return sort_data
a = transform({
            1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"],
        })
print(a)