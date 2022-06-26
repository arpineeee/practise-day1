def persent(num, per):
     return num * per / 100

def amount(money, per, year):
        i = 1
        while i <= year:
               money += persent(money, per)
               i += 1
        return money


amount_money = int(input("Enter the amount of money that you had put in the bank: "))
print(f'The amount of money in the first year: {amount(amount_money, 4, 1)}')
print(f'The amount of money in the second year: {amount(amount_money, 4, 2)}')
print(f'The amount of money in the third year: {amount(amount_money, 4, 3)}')
