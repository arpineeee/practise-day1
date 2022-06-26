s1 = float(input("Enter the firs side of your triangle: "))
s2 = float(input("Enter the second side of your triangle: "))
s3 = float(input("Enter the thired side of your triangle: "))
perimetre = s1 + s2 + s3
s = perimetre / 2 
area = (s*(s - s1)*(s - s2)*(s - s3))**(1/2) 
print(f'The area of your triangle is equal to: {area}')
