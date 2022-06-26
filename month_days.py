def day_count(year, month):
    if year % 4 == 0 and month == 2:
        return 29
    elif year % 4 != 0 and month == 2:
        return 28
    elif (month <= 7 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
        return 31
    elif (month <= 7 and month % 2 == 0) or (month >= 8 and month % 2 != 0):
        return 30
        
print(f'Number of days in the 8th month of 2022: {day_count(2022, 8)}')
