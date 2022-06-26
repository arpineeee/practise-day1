letter = input("Enter the letter: ")
if letter == "y":
    print("This letter can be vocal or consonant")
elif letter in ('a', 'e', 'o', 'u', 'i'):
    print("This letter is vocal")
else:
    print("This letter is consonant")
