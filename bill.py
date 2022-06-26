def percent(bill:float, n:int):
      """This function returns the n percent of bill"""
      return bill * n / 100
  
bill = float(input("Enter the amount of your bill: "))
print(f'The tip is equal to: {percent(bill, 18):.2f} $')
print(f'The tax is equal to: {percent(bill, 20):.2f} $')
print(f'The bill is equal to: {bill:.2f} $')
