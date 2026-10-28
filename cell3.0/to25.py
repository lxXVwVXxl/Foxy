#!/usr/bin/python3
number = int(input("Enter a number: "))
if number > 25:
    print("Even higher than 25")
else:
    for i in range(number, 26):
        print(f"inside the loop, my variable is {i}")
