def is_leap_year(year):
    leap_year_400 = (year % 400)
    leap_year_unhundred = ((year % 4) == 0) and ((year % 100) != 0)

    return (leap_year_400 == 0) or (leap_year_unhundred)


print(is_leap_year(2016))
