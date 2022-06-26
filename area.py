def area(length:float, width:float):
         """This function returns the area of the surface."""
         return length * width

length = float(input("Enter the length of your room: ")) 
width = float(input("Enter the wigth of your room: "))
print(f'The area of your room is: {area(length, width)}' "m*m")

length = float(input("Enter the length of your plot: "))
width = float(input("Enter the width of your plot: "))
print(f'The area of your plot is {(area(length, width) / 43560)} akra')
