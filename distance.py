# 1 foot = 12 inch
# 1 foot = 1 / 3 yard
# 1 foot = 1 / 5280 mile
distance = float(input("Enter the distance with foots: "))
print(f'The distance with inches is: {12 * distance} inch')
print(f'The distance with  yards is: {distance / 3} yard')
print(f'The distance with miles is: {distance / 5280} mile')
