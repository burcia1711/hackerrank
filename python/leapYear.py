def is_leap(year):
    leap = False
    if year % 4 == False:
        if year % 100 == False:
            if year % 400 == False:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap

