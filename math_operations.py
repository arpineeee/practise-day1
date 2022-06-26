def lg(num:int):
      if num == 1: 
           return 0
      res = 1
      count = 0
      while res < num:
          res *= 10
          count += 1
      return count

num1 = int(input("insert the firs number: "))
num2 = int(input("insert the second number: "))
print(f'Sum of your numbers is equal to: {num1 + num2}')
print(f'Subtraction of your numbers is equal to: {num1 - num2}')
print(f'Multiplication of your numbers is equal to: {num1 * num2}')
print(f'Integer division of your numbers is equal to: {num1 // num2}')
print(f'Residual division of your numbers is equal to: {num1 % num2}')
print(f'Division of your numbers is equal to: {num1 / num2}')
print(f'Logarithm of your numbers is equal to: {lg(num1)}')
