def egg_count(display_value):
    count = 0
    lis_var = []
    while display_value > 0:
        if display_value % 2 == 0:
            lis_var.append(0)
        else: lis_var.append(1)
        display_value =display_value // 2
    for var in lis_var:
        if var == 1:
            count += 1
    return count
a = egg_count(16)
print(a)