def sum(num:int):
     """This function returns the sum of integers in interval 1 to n."""
     sum = 0
     for num in range(0, n+1, 1):
         sum += num
     return  sum
  
n = int(input("Enter the number: "))
print(f'The sum of first {n} numbers is: {sum(n)}')
