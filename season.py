month = input("Enter the month: ")
day = int(input("Enter the day: "))
if day > 31:
    print("The day is not accurate")
elif month in ('March', 'April', 'May'):
    print("It is spring")
elif month in ('December', 'January', 'February'):
    print("It is winter")
elif month in ('June', 'July', 'August'):
    print("It is summer")
elif month in ('September', 'October', 'November'):
    print("It is autumn")
