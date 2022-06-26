# Celsius = (fahrenheit - 32) * (5 / 9)
# Fahrenheit = (9*celsius + 160) / 5
lst = [None] * 11
for i in range(11):
     k = (9*i + 160) / 5
     lst[i] = [i*10, k]

print(f'The list of fahrenheit and celsus from 0 to 100 celsius is: {lst}')
