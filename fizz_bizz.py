for i in range(1, 101):
    if i % 5 != 0 and i % 3 != 0:
        print(f'The answer is: {i}')
    elif i % 5 != 0 and i % 3 == 0:
        print("The answer is: Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("The answer is: Bizz")
    elif i % 5 == 0 and i % 3 == 0:
        print("The answer is: Fizz-Bizz")
