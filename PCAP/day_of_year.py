#!/usr/bin/env python3

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def days_in_month(year, month):
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
        return month_length[month - 1] + 1
    else:
        return month_length[month - 1]

def day_of_year(year, month, day):
    if year <= 0 or month not in range(1, 13) or day not in range(1, 32):
        return None
    s = 0
    for m in range(1, month):
        s += days_in_month(year, m)
    else:
        s += day
    return s

print(day_of_year(1989, 3, 23))
