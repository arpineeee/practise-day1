day = float(input("Enter days: "))
hour = float(input("Enter hours: "))
min = float(input("Enter hours: "))
sec = float(input("Enter seconds: "))
s = day * 12 * 3600
s1 = hour * 3600
s2 = min * 60
print(f'Your timeline with seconds is: {s + s1 + s2 + sec} sec')
