def leap_year(year):
    val_leap = False
    if year % 4 == 0:
        val_leap = True
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0 :
        val_leap = False
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0 :
        val_leap = True
    return val_leap