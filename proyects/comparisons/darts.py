def score(x, y):
    point_val= 0
    r = 0
    print(pow(x,2),y**2)
    r=(pow(x,2)+y**2)**(1/2)
    if r > 10:
        point_val = 0
    elif r > 5 and r <= 10:
        point_val = 1
    elif r > 1 and r <= 5:
        point_val = 5
    elif r >= 0 and r <= 1:
        point_val = 10
    return point_val
