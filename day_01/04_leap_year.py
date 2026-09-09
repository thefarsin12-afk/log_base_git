"""
write a program to chk year is leap year or not

"""

def leap_year(year):

    if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(f"Leap Year {year}")

    else:print(f"Not Leap Year {year}")    

leap_year(2021)