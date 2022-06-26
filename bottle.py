def sum(num1:int, num2:int):
       """This function returns the sum of bottles"""
       return num1 * 0.10 + num2 * 0.25
    
num1 = int(input("Enter the number of 1 or less liter bottles: "))   
num2 = int(input("Enter the nember of more than 1 liter bottles: "))
print(f'The sum of your bottles is ${sum(num1, num2):.2f}')
